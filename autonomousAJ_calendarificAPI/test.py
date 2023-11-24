import requests
import datetime


# Set the country and year to get holidays for
country = "US"
year = datetime.date.today().year

# API endpoint
url = "https://calendarific.com/api/v2/holidays"

# Request parameters
params = {
  "api_key": api_key,
  "country": country,
  "year": year  
}

# Make request
response = requests.get(url, params=params)

# Print out response data
data = response.json()
print(data)
for holiday in data["response"]["holidays"]:
    print(holiday["name"], holiday["date"]["iso"])