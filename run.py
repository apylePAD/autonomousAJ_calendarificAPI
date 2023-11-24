# autonomousAJ_calendarificAPI/run.py
import inquirer
from autonomousAJ_calendarificAPI.data.countries_data import Countries_Data


def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Countries', 'Holidays', 'Languages', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_countries_input():
    from autonomousAJ_calendarificAPI import test
    # country = input("Enter the name of the country: ")
    # countries_processor = Countries_Data(country)
    # countries_processor.get_and_process_countries_data()

def get_holidays_input():
    pass

def get_languages_input():
    pass


def run():
    while True:
        choice = main_menu()
        if choice == 'Countries':
            get_countries_input()
        elif choice == 'Holidays':
            get_holidays_input()
        elif choice == 'Languages':
            get_languages_input()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()