# **AI Trading Bot Data Fetcher & MongoDB and Binance API**  

This Python project retrieves real-time and historical cryptocurrency price data from the Binance API and stores it in a MongoDB database. It processes time-series data to generate **short-term (1-minute interval)** and **long-term (5-minute interval)** price trends. The script runs continuously, fetching and formatting price data for further analysis or integration with trading strategies.  

## **Features**  

- **Fetch real-time price data** from Binance API.  
- **Store and retrieve price data** in a MongoDB database.  
- **Generate short-term and long-term time-series datasets**:
  - **Short-Term:** Last 300 data points at a 1-minute interval.  
  - **Long-Term:** Last 300 data points at a 5-minute interval.  
- **Automatic data formatting** for easy visualization or model input.  
- **Continuous execution** with an interval-based update system.  

## **Technology Stack**  

- **Python 3.x**  
- **MongoDB (Atlas Cloud or Local)**  
- **Binance API (RESTful)**  
- **Requests (HTTP API calls)**  
- **Datetime & Timezone Handling**  

## **Installation & Setup**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/FatherMonkey916/AI-Trading-Bot-Data-Fetcher
cd AI-Trading-Bot-Data-Fetcher
```

### **2. Install Dependencies**  
Make sure you have Python 3 installed, then install the required libraries:  
```bash
pip install pymongo requests
```

### **3. Configure MongoDB Connection**  
Modify the MongoDB URI in the script (`MONGODB_URI`) with your credentials:  
```python
MONGODB_URI = "your_mongodb_connection_string"
```
Ensure your MongoDB database is accessible (Atlas or local).  

### **4. Run the Script**  
```bash
python main.py
```
The script will continuously fetch price data every minute and update the database.  

## **File Structure**  

```
binance-mongo-fetcher/
│── main.py               # Main script to fetch and process Binance data  
│── requirements.txt      # Python dependencies  
│── README.md             # Project documentation  
│── .gitignore            # Files to ignore in version control  
```

## **Future Enhancements**  

- Implement **error handling & logging** for better monitoring.  
- Add **support for multiple tokens** dynamically.  
- Store **additional data fields** (volume, open, high, low).  
- Develop a **web dashboard** for visualization.  

## **License**  
This project is open-source and available under the MIT License.