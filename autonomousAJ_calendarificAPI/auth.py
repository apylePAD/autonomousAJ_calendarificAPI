import os
from dotenv import load_dotenv

load_dotenv()

class Get_Calendarific_Client:
    def __init__(self):
        self.api_key = os.getenv('CALENDARIFIC_API_KEY')

    def get_calendarific_client(self):
        api_key = self.api_key
        return api_key

calendarific_client = Get_Calendarific_Client()