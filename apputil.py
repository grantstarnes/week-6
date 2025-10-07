# your code here ...
from dotenv import load_dotenv
import os

class Genius:
    def __init__(self, access_token=None):
        # Load environment variables
        load_dotenv()

        # Assign the token (from argument or .env)
        self.access_token = access_token or os.getenv("ACCESS_TOKEN")

        # If no token found, raise an error
        if not self.access_token:
            raise ValueError("Genius access token must be provided or set in environment variables.")

        # Base URL and headers
        self.base_url = "https://api.genius.com"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
