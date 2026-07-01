import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from fetch_data import get_data
from indicators import add_indicators
from backtester import backtest_strategy

st.title("🚀 BTC Signal Dashboard")

# Fetch and process data
df = get_data(limit=500)
df = add_indicators(df)

# Run backtest
win_rate, df_results = backtest_strategy(df)

# Display on the Dashboard
st.metric("Historical Strategy Return", f"{win_rate:.2%}")
st.line_chart(df_results["close"])
st.write("Data Preview:", df_results.tail())
