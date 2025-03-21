import pymongo
from datetime import datetime, timezone

# MongoDB Connection
MONGODB_URI = "mongodb+srv://alertdb:NzRoML9MhR3sSKjM@cluster0.iittg.mongodb.net/alert3"
client = pymongo.MongoClient(MONGODB_URI)
db = client["alert3"]

def fetch_token_data(db, token):
    """
    Fetches long and short time-series data for a given token.
    - Long: 300 data points, every 5 minutes from the most recent.
    - Short: 300 data points, every 1 minute from the most recent.
    """
    collection = db[f"{token}_timeseries"]
    now = datetime.now(timezone.utc)
    
    # Fetch 300 most recent 5-minute interval data
    long_data = list(collection.find()
        .sort("timestamp", -1)  # Sort descending (latest first)
        .limit(300 * 5)  # Get extra data to filter
    )
    long_data = long_data[::-1][::5]  # Keep every 5th entry
    
    # Fetch 300 most recent 1-minute interval data
    short_data = list(collection.find()
        .sort("timestamp", -1)
        .limit(300)  # Get exact 300 records
    )[::-1]  # Reverse to chronological order
    
    # Format output
    formatted_long = [{
        "ds": entry["timestamp"],
        "unique_id": entry["token"],
        "y": entry["price"]
    } for entry in long_data]
    
    formatted_short = [{
        "ds": entry["timestamp"],
        "unique_id": entry["token"],
        "y": entry["price"]
    } for entry in short_data]
    
    return {"long": formatted_long, "short": formatted_short}

if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        TARGET_TOKEN = "BTCUSDT"  # Change this to select a different token
        token_data = fetch_token_data(db, TARGET_TOKEN)
        print(token_data)
    except Exception as e:
        print(f"Error: {e}")
