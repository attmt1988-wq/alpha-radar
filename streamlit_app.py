import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Alpha Radar - US Stock Scanner")

stocks = ["NVDA","AMD","TSLA","META","AAPL","PLTR"]

results = []

for ticker in stocks:
    data = yf.download(ticker, period="1d", interval="5m")

    if len(data) == 0:
        continue

    price = data["Close"].iloc[-1]
    volume = data["Volume"].iloc[-1]

    results.append({
        "Stock": ticker,
        "Price": round(price,2),
        "Volume": int(volume)
    })

df = pd.DataFrame(results)

st.dataframe(df)
