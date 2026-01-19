import logging
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()



# configure 
logging.basicConfig(

    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)#
url = "https://alpha-vantage.p.rapidapi.com/query"
headers = {
	"x-rapidapi-key": "7d30a91722mshad437fcfd538d21p19c033jsn388fd745dbf9",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}