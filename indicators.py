from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

def add_indicators(df):
    df["sma_fast"] = SMAIndicator(df["close"], window=7).sma_indicator()
    df["sma_slow"] = SMAIndicator(df["close"], window=25).sma_indicator()
    df["rsi"] = RSIIndicator(df["close"], window=14).rsi()
    return df