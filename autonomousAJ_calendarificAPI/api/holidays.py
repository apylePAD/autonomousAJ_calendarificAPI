# autonomousAJ_calendarificAPI/api/holidays.py
import requests
from .base import Calendarific_API_Base

class Holidays(Calendarific_API_Base):
    def search_holidays(self):
        api_key = self.get_calendarific_client()
        print(api_key)

        # Endpoint for getting a random recipe
        url = "https://calendarific.com/api/v2/holidays"

        # Parameters for the API call
        params = {
            'apiKey': api_key,
        }

        # Making the GET request
        response = requests.get(url, params=params)

        # Checking if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data)  # or process the data as you need
        else:
            print("Failed to retrieve data:", response.status_code)

        return data
