def generate_signal(df):
    latest = df.iloc[-1]
    if latest["sma_fast"] > latest["sma_slow"] and latest["rsi"] < 70:
        return "UP"
    elif latest["sma_fast"] < latest["sma_slow"] and latest["rsi"] > 30:
        return "DOWN"
    else:
        return "HOLD"