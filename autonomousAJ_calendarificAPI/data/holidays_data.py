# autonomousAJ_calendarificAPI/data/holidays_data.py
from datetime import datetime
import pandas as pd
from autonomousAJ_calendarificAPI.api.holidays import Holidays
from autonomousAJ_calendarificAPI.config import global_config

class Holidays_Data:
    def __init__(self):
        self.calendarific_holidays = Holidays()

    def get_and_process_holidays_data(self):
        holidays_data = self.calendarific_holidays.search_holidays()
        
        df_holidays = pd.json_normalize(holidays_data['recipes']['items'])
        self.save_holidays_data(df_holidays)

    def save_holidays_data(self, df_holidays):
        now = datetime.now()
        df_holidays.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/holidays/holidays_{now}.csv", index=False)
        print(df_holidays)

