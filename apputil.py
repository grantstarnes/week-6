# your code here ...
from dotenv import load_dotenv
import os
import requests
class Genius:
    def __init__(self, access_token=None):
        '''
        This function takes in an access_token, whether manually entered, or in this instance, pulled from
        'ACCESS_TOKEN' from the .env file. It then assigns a base url to the genius api site in variable self.base_url.
        This self.base_url also helps throughout the remainder of the exercises as we don't have to type the url repeatedly.
        '''
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
        '''
        This function takes in a search_term, in the example, "Radiohead," from the Genius website. 
        It then accesses the artist_id and api_path and retrieves the data for that artist. Lastly,
        it returns a dictionary of the artist data as the output.
        '''

        # search through genius
        search_url = f"{self.base_url}/search"

        headers = self.headers

        params = {'q': search_term}

        response = requests.get(search_url, headers=headers, params=params)

        json_data = response.json()

        # moves through the dictionary to get to the artist data
        api_path = json_data['response']['hits'][0]['result']['primary_artist']['api_path']

        # accesses the artist_id
        artist_id = api_path.split('/')[-1]
    
        artist_url = f"{self.base_url}{api_path}"
        artist_response = requests.get(artist_url, headers=headers)
        artist_data = artist_response.json()

        # returns a dictionary of data for the searched artist
        return artist_data