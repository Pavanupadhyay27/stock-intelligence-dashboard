from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response, StreamingResponse
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import io
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

app = FastAPI()

# List of companies
COMPANIES = [
    "TSLA",
    "AAPL",
    "MSFT",
    "INFY.NS",
    "TCS.NS",
    "RELIANCE.NS",
    "META",
    "GOOGL",
    "AMZN"
]

# Serve frontend files from 'web' folder
app.mount("/web", StaticFiles(directory="web"), name="web")

@app.get("/")
def home():
    return {"msg": "Stock API is running. Visit /web/index.html for dashboard."}

@app.get("/companies")
def list_companies():
    return {"companies": COMPANIES}

# Fetch stock data helper function
def fetch_data(symbol):
    df = yf.download(symbol, start='2023-01-01', end='2023-12-31')
    if df.empty:
        return pd.DataFrame()
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]
    df = df.reset_index().dropna()
    df['Daily Return'] = (df['Close'] - df['Open']) / df['Open']
    df['7d MA'] = df['Close'].rolling(window=7).mean()
    if 'Date' in df.columns:
        df['Date'] = df['Date'].astype(str)
    if 'Datetime' in df.columns:
        df['Datetime'] = df['Datetime'].astype(str)
    return df

@app.get("/data")
def get_data(symbol: str = Query("TSLA"), period: int = Query(30)):
    df = fetch_data(symbol)
    if df.empty:
        return []
    df.columns = [str(col) for col in df.columns]
    df = df.tail(period)
    df = df.replace({np.nan: None})
    return df.to_dict(orient='records')

@app.get("/summary")
def get_summary(symbol: str = Query("TSLA")):
    df = fetch_data(symbol)
    if df.empty:
        return {"symbol": symbol, "error": "No data found for this symbol"}
    return {
        "symbol": symbol,
        "52w_high": float(df['Close'].max()),
        "52w_low": float(df['Close'].min()),
        "average_close": float(df['Close'].mean())
    }

# ---- New /predict endpoint ----
@app.get("/predict")
def predict(symbol: str = Query("TSLA")):
    df = fetch_data(symbol)
    if df.empty or 'Close' not in df.columns:
        return {"symbol": symbol, "error": "No data available for prediction"}
    df = df.reset_index(drop=True)
    # Use day index as feature
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['Close'].values
    model = LinearRegression()
    model.fit(X, y)
    last_index = len(df) - 1
    future_indices = np.array(range(last_index + 1, last_index + 8)).reshape(-1, 1)
    preds = model.predict(future_indices)
    # Dates
    if 'Date' in df.columns:
        last_date = datetime.strptime(df['Date'].iloc[-1], "%Y-%m-%d")
    else:
        last_date = datetime.today()
    future_dates = [(last_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 8)]
    result = [{"Date": d, "Predicted_Close": float(p)} for d, p in zip(future_dates, preds)]
    return {"symbol": symbol, "forecast": result}
# ---- End of new endpoint ----

# ---- New /correlation endpoint ----
@app.get("/correlation")
def correlation(symbol1: str = Query(...), symbol2: str = Query(...)):
    df1 = fetch_data(symbol1)
    df2 = fetch_data(symbol2)
    if df1.empty or df2.empty:
        return {"error": f"No data for one or both symbols: {symbol1}, {symbol2}"}
    # Merge on date for safety
    merged = pd.merge(df1[["Date", "Close"]], df2[["Date", "Close"]], on="Date", suffixes=(f"_{symbol1}", f"_{symbol2}"))
    if merged.empty:
        return {"error": "No overlapping dates for correlation analysis."}
    corr = merged[f'Close_{symbol1}'].corr(merged[f'Close_{symbol2}'])
    return {
        "symbol1": symbol1,
        "symbol2": symbol2,
        "correlation": corr
    }
# ---- End correlation ----

@app.get("/compare")
def compare(symbol1: str = Query(...), symbol2: str = Query(...)):
    df1 = fetch_data(symbol1)
    df2 = fetch_data(symbol2)
    if df1.empty or df2.empty:
        return {"error": "One or both symbols returned no data"}
    avg1 = float(df1['Close'].mean())
    avg2 = float(df2['Close'].mean())
    return {
        "symbol1": symbol1,
        "average_close1": avg1,
        "symbol2": symbol2,
        "average_close2": avg2,
        "avg_diff": avg1 - avg2
    }

@app.get("/volatility")
def volatility(symbol: str = "TSLA"):
    df = fetch_data(symbol)
    if df.empty:
        return {"symbol": symbol, "error": "No data found"}
    vol = float(df['Close'].std())
    return {"symbol": symbol, "volatility": vol}

@app.get("/download")
def download_data(symbol: str = "TSLA"):
    df = fetch_data(symbol)
    if df.empty:
        return Response(content="Symbol not found or no data.", media_type="text/plain")
    csv_str = df.to_csv(index=False)
    return Response(content=csv_str, media_type="text/csv")

@app.get("/plot")
def plot_data(symbol: str = "TSLA"):
    df = fetch_data(symbol)
    if df.empty:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"No data for {symbol}", ha='center', va='center')
    else:
        fig, ax = plt.subplots()
        ax.plot(df['Date'] if 'Date' in df.columns else df.index, df['Close'])
        ax.set_title(f'Closing Price: {symbol}')
        plt.xticks(rotation=45)
        plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return StreamingResponse(buf, media_type="image/png")

