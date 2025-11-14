# stock-intelligence-dashboard
A modern, interactive Stock Intelligence Dashboard powered by FastAPI and Plotly. Provides real-time analytics, price trends, and machine learning forecasts for major global companies using live financial data. Includes RESTful APIs, modular backend, and a user-friendly web interface for deep stock insights and interactive visualization.

Table of Contents
Features

Setup Instructions

Project Structure

Core Logic & API Endpoints

Frontend Dashboard Overview

Insights & Example Analytics

Extending/Deployment

Credits

Features
Live stock data via Yahoo Finance API (yfinance)

RESTful backend APIs for data retrieval, statistics, trend forecasting, comparison, and volatility

Interactive dashboard for data and chart visualization

Linear regression-based 7-day price predictions

Data download/export (.csv)

Modular, scalable and easy to run locally

Setup Instructions
Prerequisites:

Python 3.8 or higher

Steps:

Clone the repository

bash
git clone https://github.com/Pavanu padhyay27/stock-intelligence-dashboard
cd stock-intelligence-dashboard
Create and activate a virtual environment (recommended)

bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run the backend API server

bash
uvicorn app:app --reload
Open your browser and visit:

text
http://127.0.0.1:8000/web/index.html
Project Structure
text
.
├── app.py
├── requirements.txt
├── web/
│   └── index.html
└── README.md
Core Logic & API Endpoints
Backend:
Built using FastAPI, Pandas, and scikit-learn.

/companies: Returns supported stock symbols.

/data: Returns historical price & volume data for a company.

/summary: Returns 52-week high/low/average close.

/predict: Returns a 7-day price forecast (linear regression).

/correlation: Returns Pearson correlation between two companies.

/compare: Compares average closing price between two companies.

/volatility: Returns the standard deviation of daily close prices.

/download: Download full price history as CSV.

/plot: Returns a static closing price plot image.

Key data processing steps:

Data fetched using yfinance, cleaned with Pandas

New columns created: Daily Return, 7-day Moving Average

Forecast uses scikit-learn LinearRegression on time-indexed price series

Frontend Dashboard Overview
Company selector: View data for TSLA, MSFT, INFY.NS, TCS.NS, RELIANCE.NS, META, GOOGL, AAPL, AMZN

Period filter: Choose last 30, 90, or 365 days

Key stats panel: 52-week high, low, average close

Charts: Interactive Plotly chart of price and volume

Show 7-Day Forecast: Generates and plots predicted prices for upcoming days

Insights & Example Analytics
Each dashboard view offers distinct business insights.
Keep the tone professional—sample summaries provided below for your screenshots or detailed analysis:

TSLA (Tesla)
Summary: TSLA has demonstrated significant volatility throughout 2023, with multiple peaks and corrections. The 52-week range emphasizes its role as a growth-oriented but unpredictable asset. Price forecasts indicate a short-term upswing aligned with current momentum and volume trends.

MSFT (Microsoft)
Summary: MSFT illustrates strong and consistent growth, with limited sharp declines. The correlation analysis with other tech giants can identify diversification opportunities for portfolios. Moving average smooths minor daily fluctuations, revealing a resilient uptrend.

RELIANCE.NS (Reliance Industries)
Summary: The price trajectory reflects industry-wide events and sectoral shifts. Notable periods of volume spikes correspond to market-wide news. Volatility score should be considered by investors seeking exposure in emerging markets.

AAPL (Apple)
Summary: Apple's steady climb and moderate volatility suggest strong investor confidence. The prediction model projects continued growth.

INFY.NS, TCS.NS (Indian IT Majors)
Summary: Both INFY and TCS show sectoral stability and healthy average closes. Weekly moving averages help visualize earnings and dividend impacts.

META (Meta/Facebook), GOOGL (Alphabet/Google), AMZN (Amazon)
Summary: All three display classic large-cap tech movement—periods of growth, correction, and recovery. Forecasts and correlation analyses provide valuable context for multi-asset strategies.
