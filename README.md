## AI Trading Bot Data Fetcher

This project is an essential component for AI modeling in the development of an AI trading bot. It provides a robust mechanism to fetch and format time-series data for cryptocurrency tokens from a MongoDB database.

### Key Features:

1. **MongoDB Integration**: Connects to a MongoDB Atlas cluster to retrieve real-time cryptocurrency data.
2. **Dual Time-Series Fetching**: 
   - Long-term data: Retrieves 300 data points at 5-minute intervals.
   - Short-term data: Fetches 300 data points at 1-minute intervals.
3. **Data Formatting**: Structures the data in a format suitable for AI model training and analysis.
4. **Flexible Token Selection**: Easily adaptable to fetch data for different cryptocurrency pairs.

### Use Case:

This tool is designed to support the development of AI trading bots by providing clean, structured data for model training and real-time predictions. It can be integrated into larger systems for cryptocurrency market analysis, backtesting trading strategies, and live trading implementations.

### Technical Details:

- **Language**: Python
- **Database**: MongoDB
- **Key Libraries**: pymongo, datetime

### Getting Started:

1. Clone the repository
2. Install required dependencies: `pip install pymongo`
3. Set up your MongoDB connection string in the `MONGODB_URI` variable
4. Run the script to fetch data for a specific token (default is BTCUSDT)

### Future Enhancements:

- Add support for multiple tokens in a single query
- Implement error handling and retry mechanisms for robust data fetching
- Create a configuration file for easy customization of database settings and token selection

This project serves as a foundational component for AI-driven cryptocurrency trading systems, providing clean and structured data essential for accurate model training and real-time decision making.
