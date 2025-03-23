import pymongo
from datetime import datetime, timezone, timedelta
import time
import requests

BINANCE_API_URL = "https://api.binance.com/api/v3/klines"

def fetch_price_data(token, start_time, end_time, interval="1m"):
    """
    Fetch price data from Binance API for a specific token and interval.
    """
    params = {
        "symbol": token,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": 5 if interval == "5m" else 1
    }
    response = requests.get(BINANCE_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return []

def fetch_token_data(db, token):
    """
    Fetches time-series data for a given token.
    - Long: 300 data points (299 from DB, 1 from API), continuous intervals.
    - Short: 300 data points (299 from DB, 1 from API).
    """
    collection = db[f"{token}_timeseries"]
    now = datetime.now(timezone.utc)
    
    # Fetch latest short item using API
    previous_minute = now.replace(second=0, microsecond=0) - timedelta(minutes=1)
    start_time = int(previous_minute.timestamp() * 1000)
    end_time = start_time + 60 * 1000 - 1
    short_api_data = fetch_price_data(token, start_time, end_time)
    
    # Fetch 299 most recent 1-minute interval data from DB
    short_db_data = list(collection.find().sort("timestamp", -1).limit(299))[::-1]
    # Format short data
    formatted_short = [{
        "ds": entry["timestamp"] + timedelta(minutes=1),
        "unique_id": entry["token"],
        "y": entry["close"]
    } for entry in short_db_data]
    # Append latest short item from API
    if short_api_data:
        formatted_short.append({
            "ds": datetime.fromtimestamp(short_api_data[0][0] / 1000, timezone.utc) + timedelta(minutes=1),
            "unique_id": token,
            "y": float(short_api_data[0][4])  # Close price
        })
    # Fetch latest long item using API (average of last 5 minute items)
    long_api_prices = []
    for i in range(5):
        minute_time = previous_minute - timedelta(minutes=i)
        start_time = int(minute_time.timestamp() * 1000)
        end_time = start_time + 60 * 1000 - 1
        price_data = fetch_price_data(token, start_time, end_time)
        if price_data:
            long_api_prices.append(float(price_data[0][4]))  # Close price
    if long_api_prices:
        long_api_avg_price = sum(long_api_prices) / len(long_api_prices)
        long_api_data = {
            "ds": previous_minute + timedelta(minutes=1),
            "unique_id": token,
            "y": long_api_avg_price
        }
    else:
        long_api_data = None
    # Fetch 299 most recent 1-minute interval data from DB and calculate long items
    long_db_data = list(collection.find().sort("timestamp", -1).limit(299 + 4))[::-1]
    formatted_long = []
    for i in range(len(long_db_data) - 4):
        five_min_chunk = long_db_data[i:i+5]
        avg_price = sum(entry["close"] for entry in five_min_chunk) / 5
        formatted_long.append({
            "ds": five_min_chunk[-1]["timestamp"] + timedelta(minutes=1),
            "unique_id": token,
            "y": avg_price
        })
    # Append latest long item from API
    if long_api_data:
        formatted_long.append(long_api_data)
    
    return {"long": formatted_long, "short": formatted_short}

if __name__ == "__main__":
    # MongoDB Connection
    MONGODB_URI = "mongodb+srv://alertdb:NzRoML9MhR3sSKjM@cluster0.iittg.mongodb.net/alert3"
    client = pymongo.MongoClient(MONGODB_URI)
    db = client["alert3"]
    
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        TARGET_TOKEN = "BTCUSDT"
        while True:
            now = datetime.now(timezone.utc)
            if now.second == 0:
                token_data = fetch_token_data(db, TARGET_TOKEN)
                print(token_data)
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
