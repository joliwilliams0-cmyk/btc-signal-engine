import requests
import pandas as pd

# In fetch_data.py
def get_data(limit=500, interval='1d'):
    url = f'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval={interval}&limit={limit}'
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"API Error: {response.status_code} - {response.text}") # Look at this in your logs
        return pd.DataFrame()
    
    # ... rest of your code
    
    data = response.json()
    
    # Binance returns data in a specific list format
    columns = [
        'open_time', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ]
    
    df = pd.DataFrame(data, columns=columns)
    
    # Clean and format the data
    df['close'] = df['close'].astype(float)
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['volume'] = df['volume'].astype(float)
    df['time'] = pd.to_datetime(df['open_time'], unit='ms')
    
    return df[['time', 'open', 'high', 'low', 'close', 'volume']]
