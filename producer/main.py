from extract import connect_to_api, extract_json
from producer_setup import init_producer, topic
import time


def main():
    producer = init_producer()  # Initialize producer
    
    try:
        while True:
            print("\n--- Fetching stock data ---")
            response = connect_to_api()

            if response is None:
                print("Failed to fetch data from API")
                time.sleep(60)  # Wait 60 seconds before retrying
                continue

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

                try:
                    producer.send(topic, result)
                    print(f'Data sent: {stock["symbol"]} - {stock["date"]}')
                except Exception as e:
                    print(f'Error sending data: {e}')

            producer.flush()
            print(f"Sent {len(data)} records. Waiting 300 seconds before next fetch...")
            time.sleep(60) # Wait 60 seconds before next fetch
    
    except KeyboardInterrupt:
        print("\nShutting down producer...")
    finally:
        producer.close()
        print("Producer closed.")


if __name__ == "__main__":
    main()