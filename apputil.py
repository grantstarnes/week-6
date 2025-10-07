# your code here ...
from dotenv import load_dotenv
import os
import requests
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
        self.base_url = "http://api.genius.com"
        self.headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

    def get_artist(self, search_term):
        search_url = f"{self.base_url}/search"
        headers = self.headers
        params = {'q': search_term}
        response = requests.get(search_url, headers=headers, params=params)
        json_data = response.json()
    
        api_path = json_data['response']['hits'][0]['result']['primary_artist']['api_path']
        artist_id = api_path.split('/')[-1]
    
        artist_url = f"{self.base_url}{api_path}"
        artist_response = requests.get(artist_url, headers=headers)
        artist_data = artist_response.json()
    
        return artist_data