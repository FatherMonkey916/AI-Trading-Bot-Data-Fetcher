# AI Trading Bot Data Fetcher with MongoDB and Binance API

## Overview
This project fetches real-time cryptocurrency price data from the Binance API and stores it in MongoDB. It continuously retrieves the latest price every minute and processes historical data to generate long-interval price averages. The script ensures efficient data retrieval by fetching only new price data from Binance while utilizing stored historical data for long-term calculations.

## Features
- **Fetches real-time price data** for a specified cryptocurrency from Binance API.
- **Stores and retrieves price data** from MongoDB for efficient processing.
- **Generates short-term (1-minute) and long-term (5-minute average) price series**.
- **Ensures continuous, non-overlapping long-term price data.**
- **Runs continuously**, updating every minute when the system clock hits `00` seconds.

## Prerequisites
Before running the script, ensure you have the following:
- **Python 3.7+**
- **MongoDB Atlas or a local MongoDB instance**
- **Required Python libraries:**
  ```sh
  pip install pymongo requests
  ```
- **A valid MongoDB connection URI**

## Installation & Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/FatherMonkey916/AI-Trading-Bot-Data-Fetcher
   cd AI-Trading-Bot-Data-Fetcher
   ```

2. **Configure MongoDB Connection:**
   - Open the script and update the `MONGODB_URI` variable with your MongoDB connection string.

3. **Run the script:**
   ```sh
   python fetch_prices.py
   ```

## How It Works
- The script connects to MongoDB and ensures the database is reachable.
- It continuously fetches price data from Binance and stores it in MongoDB.
- It retrieves **short-term data (1-minute intervals)** from the database and appends the latest API data.
- It calculates **long-term data (5-minute averages)** using stored and new data.
- The script runs in a loop, fetching and processing data only when the current second is `00`.

## Data Format
Each fetched price entry follows this structure:
```json
{
  "ds": "2024-03-24T11:21:00Z",  // Timestamp of the data point
  "unique_id": "BTCUSDT",         // Token identifier
  "y": 65743.5                    // Closing price
}
```

## Contribution
Feel free to contribute by submitting issues or pull requests. Ensure you follow best coding practices and test your changes before submission.

## License
This project is open-source and available under the **MIT License**.

---

> **Note:** Update the repository URL before pushing the project to GitHub.

