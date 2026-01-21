import requests
from config import logger, url, headers


def connect_to_api():
    stocks = [ "MSFT", "GOOGL",  "TSLA"]
    json_responses = []
    for stock in range(len(stocks)):
        querystring = {
            "function":"TIME_SERIES_INTRADAY",
            "symbol": f"{stocks[stock]}",
            "outputsize":"compact",
            "interval":"5min",
            "datatype":"json"}

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            logger.info(f"{stocks[stock]} Stocks data retrieved successfully ")
            json_responses.append(data)
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to API: {e}")
            return None
    
    return json_responses
def extract_json(response):
    records = []
    for data in response:
        symbol = data["Meta Data"]["2. Symbol"]

        for date_str, metrics in data['Time Series (5min)'].items():
            record = {
                "symbol": symbol,
                "date": date_str,
                "open": float(metrics["1. open"]),
                "high": float(metrics["2. high"]),
                "low": float(metrics["3. low"]),
                "close": float(metrics["4. close"])
            }
            records.append(record)
    return records
    