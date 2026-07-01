import sys
import os
import streamlit as st

# Configure path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from fetch_data import get_data
from indicators import add_indicators
from backtester import backtest_strategy

st.title("🚀 BTC Signal Dashboard")

# Fetch and process data
df = get_data(limit=500)

if df.empty:
    st.error("Error: Failed to fetch data. The DataFrame is empty.")
    st.stop()

# Analyze and display
df = add_indicators(df)
st.write("Data fetched and indicators added successfully.")

win_rate, df_results = backtest_strategy(df)

# Dashboard Layout
st.metric("Historical Strategy Return", f"{win_rate:.2%}")
st.line_chart(df_results["close"])
st.write("Data Preview:", df_results.tail())
