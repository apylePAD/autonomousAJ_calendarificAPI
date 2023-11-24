# autonomousAJ_calendarificAPI/data/languages_data.py
from datetime import datetime
import pandas as pd
from autonomousAJ_calendarificAPI.api.languages import Languages
from autonomousAJ_calendarificAPI.config import global_config

class Languages_Data:
    def __init__(self):
        self.calendarific_languages = Languages()

    def get_and_process_languages_data(self):
        languages_data = self.calendarific_languages.search_languages()
        
        df_languages = pd.json_normalize(languages_data['recipes']['items'])
        self.save_languages_data(df_languages)

    def save_languages_data(self, df_languages):
        now = datetime.now()
        df_languages.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/languages/languages_{now}.csv", index=False)
        print(df_languages)

