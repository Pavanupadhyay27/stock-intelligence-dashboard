📊 Stock Intelligence Dashboard

A modern, interactive stock analytics platform powered by FastAPI, Plotly, and Machine Learning.
It delivers historical trends, correlation analysis, forecasts, volatility metrics, and more — all wrapped in a clean, user-friendly dashboard.

📌 Table of Contents

Features

Setup Instructions

Project Structure

Core Logic & API Endpoints

Frontend Dashboard Overview

Insights & Example Analytics

🚀 Features

Live stock market data using Yahoo Finance (yfinance)

RESTful API with scalable FastAPI endpoints

Interactive dashboard built with HTML, CSS & Plotly

Linear Regression model for 7-day price predictions

Correlation analysis between any two stocks

Volatility measurement, comparison metrics, and summary statistics

Clean, modular backend with clearly separated routes

CSV export, dynamic charts, and interactive data visualization

Lightweight, easy to deploy, and beginner-friendly

⚙️ Setup Instructions
Prerequisites

Python 3.8+

1. Clone the Repository
git clone https://github.com/Pavanupadhyay27/stock-intelligence-dashboard
cd stock-intelligence-dashboard

2. Create & Activate Virtual Environment
python -m venv venv


Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run FastAPI Server
uvicorn app:app --reload

5. Open Dashboard

Visit in browser:

http://127.0.0.1:8000/web/index.html

🗂 Project Structure
.
├── app.py                 # Backend API (FastAPI)
├── requirements.txt       # Python dependencies
├── web/
│   └── index.html         # Frontend dashboard (Plotly)
└── README.md

🧠 Core Logic & API Endpoints

Backend uses FastAPI, Pandas, yfinance, and scikit-learn.

Available Endpoints
Endpoint	Description
/companies	List of supported stock symbols
/data	Historical data (Open, Close, Volume)
/summary	52-week high, 52-week low, average close
/predict	ML-based 7-day price forecast
/correlation	Pearson correlation of two stock trends
/compare	Compare two stocks’ average close prices
/volatility	Standard deviation of closing prices
/download	Export full dataset as CSV
/plot	Static PNG plot of closing price

🔍 Key Data Processing Steps

Fetches data using yfinance
Cleans missing values & normalizes columns
Computes:
Daily Returns
7-Day Moving Average
Linear Regression forecasting using time-indexed price series
Converts results to JSON for frontend visualization

🖥️ Frontend Dashboard Overview
What Users Can Do

Select companies:
TSLA, MSFT, INFY.NS, TCS.NS, RELIANCE.NS, META, GOOGL, AAPL, AMZN

Filter data by period: 30 / 90 / 365 days

View:

Interactive closing price charts

Volume overlays

Key statistics

Generate a 7-Day forecast using ML

Analyze trends visually through Plotly charts

📈 Insights & Example Analytics

<img width="1919" height="914" alt="image" src="https://github.com/user-attachments/assets/c903eac9-7c7f-456d-bf42-17b0b33e0de6" />
<img width="1904" height="905" alt="image" src="https://github.com/user-attachments/assets/15a3b832-e8a6-47d4-abb2-a11f11d0beee" />
<img width="1907" height="897" alt="image" src="https://github.com/user-attachments/assets/847e430a-b813-4119-8551-d84ccbc8aeb8" />
<img width="1919" height="899" alt="image" src="https://github.com/user-attachments/assets/e9b64468-b129-4697-812c-6ce169778c69" />
<img width="1917" height="885" alt="image" src="https://github.com/user-attachments/assets/13660528-01ac-475d-ba78-76c97814b33f" />





📌 TSLA (Tesla)

Tesla shows high volatility and aggressive price swings throughout 2023.
Patterns indicate speculative trading behavior and strong sensitivity to market news.
Forecasts typically project short-term upward momentum after strong volume buildup.

📌 MSFT (Microsoft)

Microsoft maintains a stable upward trend with low volatility.
Its 52-week range shows consistent investor confidence and minimal corrective dips.
Correlation with other tech giants provides insights for portfolio diversification.

📌 RELIANCE.NS (Reliance Industries)

Price movement reflects sector-driven trends in energy and telecom markets.
Volume spikes often align with corporate announcements or policy changes.
Volatility is moderate, suitable for medium-risk portfolios.

📌 AAPL (Apple)

Apple demonstrates a smooth growth trajectory with controlled volatility.
Weekly moving averages indicate strong institutional support.
Forecasts often extend the ongoing slow-and-steady climb.

📌 Indian IT: INFY.NS / TCS.NS

Both companies show sectoral stability, with predictable earnings cycles.
Moving averages reveal periodic dips during earnings announcements.
Good examples of low-volatility tech investments.

📌 META, GOOGL, AMZN

These companies exhibit:

High liquidity

Strong correlation inside the tech sector

Clear long-term growth with short-term volatilitysic large-cap tech movement—periods of growth, correction, and recovery. Forecasts and correlation analyses provide valuable context for multi-asset strategies.
