import pandas as pd

def backtest_strategy(df):
    df['signal'] = 'HOLD'
    for i in range(1, len(df)):
        if df['sma_fast'].iloc[i] > df['sma_slow'].iloc[i] and df['rsi'].iloc[i] < 70:
            df.at[df.index[i], 'signal'] = 'BUY'
        elif df['sma_fast'].iloc[i] < df['sma_slow'].iloc[i] and df['rsi'].iloc[i] > 30:
            df.at[df.index[i], 'signal'] = 'SELL'
            
    df['returns'] = df['close'].pct_change()
    df['strategy_returns'] = df['returns'].shift(-1) * (df['signal'] == 'BUY')
    total_return = (1 + df['strategy_returns']).prod() - 1
    return total_return, df