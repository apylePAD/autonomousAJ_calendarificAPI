# autonomousAJ_calendarificAPI/data/countries_data.py
from datetime import datetime
import pandas as pd
from autonomousAJ_calendarificAPI.api.countries import Countries
from autonomousAJ_calendarificAPI.config import global_config

class Countries_Data:
    def __init__(self, country):
        self.country = country
        self.calendarific_countries = Countries()

    def get_and_process_countries_data(self):
        countries_data = self.calendarific_countries.get_countries(self.country)
        
        df_countries = pd.json_normalize(countries_data['recipes']['items'])
        self.save_countries_data(df_countries)

    def save_countries_data(self, df_countries):
        now = datetime.now()
        df_countries.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/countries/countries_{now}.csv", index=False)
        print(df_countries)

