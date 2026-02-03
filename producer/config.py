import logging
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()



# configure 
logging.basicConfig(

    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BASEURL = "alpha-vantage.p.rapidapi.com"

api_key = os.getenv("API_KEY")



url = f"https://{BASEURL}/query"
headers = {
	"x-rapidapi-key": api_key,
	"x-rapidapi-host": BASEURL
}