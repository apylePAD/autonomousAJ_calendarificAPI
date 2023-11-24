# autonomousAJ_calendarificAPI/api/countries.py
import requests
import datetime
from .base import Calendarific_API_Base

class Countries(Calendarific_API_Base):
    def get_countries(self, country):
        api_key = self.get_calendarific_client()
        year = datetime.date.today().year

        print(api_key)

        # Endpoint for getting a random recipe
        url = "https://calendarific.com/api/v2/holidays"

        # Parameters for the API call
        params = {
            'apiKey': api_key,
            'country': country,
            'year': year,
        }

        # Making the GET request
        response = requests.get(url, params=params)
        print(response)

        # Checking if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)  # or process the data as you need
        else:
            print("Failed to retrieve data:", response.status_code)

        return data
