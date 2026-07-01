import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from fetch_data import get_data
from indicators import add_indicators
from backtester import backtest_strategy

st.title("🚀 BTC Signal Dashboard")

# app.py
df = get_data(limit=500)

if df.empty:
    st.error("Error: Failed to fetch data. The DataFrame is empty.")
    st.stop() # This stops the app execution here so it doesn't crash on indicators

df = add_indicators(df)
st.write("Data fetched:", len(df))

df = add_indicators(df)
st.write("Data after indicators:", len(df))

win_rate, df_results = backtest_strategy(df)
st.write("Results after backtest:", len(df_results))
# Display on the Dashboard
st.metric("Historical Strategy Return", f"{win_rate:.2%}")
st.line_chart(df_results["close"])
st.write("Data Preview:", df_results.tail())
