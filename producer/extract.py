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
        logger.info(f"Stocks data retrieved successfully for")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error connecting to API: {e}")
        return None
    
    