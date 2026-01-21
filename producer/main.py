from extract import connect_to_api, extract_json



def main():
    response = connect_to_api()

    data = extract_json(response)

    for stock in data:
        result = {
            "symbol": stock["symbol"],
            "date": stock["date"],
            "open": stock["open"],
            "high": stock["high"], 
            "low": stock["low"],
            "close": stock["close"]
        }

        print(result)
    return None

if __name__ == "__main__":
    main()