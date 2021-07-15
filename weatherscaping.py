import requests
from bs4 import BeautifulSoup
import pandas as pd


city = str(input("Enter the name of the city you want the weather forecast for: "))

url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"

site = requests.get(url)
list = []
soup = BeautifulSoup(site.content, "lxml")

weather_items = soup.find("tr", class_= "b-forecast__table-weather js-weather")
weather = weather_items.find_all('td') 

max_temp_items = soup.find("tr", class_="b-forecast__table-max-temperature js-temp")
max_temp = max_temp_items.find_all('td')

min_temp_items = soup.find("tr", class_="b-forecast__table-min-temperature js-min-temp")
min_temp = min_temp_items.find_all('td')

humidity_items = soup.find("tr", class_="b-forecast__table-humidity js-humidity")
humidity = humidity_items.find_all('td')

uv_items = soup.find("tr", class_="b-forecast__table-uv js-uv")
uv = uv_items.find_all('td')

sunrise_items = soup.find("tr", class_="b-forecast__table-sunrise js-sunrise")
sunrise = sunrise_items.find_all('td')

sunset_items = soup.find("tr", class_="b-forecast__table-sunset js-sunset")
sunset = sunset_items.find_all('td')

for i in range(12):
    dict = {}
    dict["day"] = soup.find_all('div',{"class":'b-forecast__table-days-name'})[i].text
    dict["date"] = soup.find_all('div',{"class":'b-forecast__table-days-date'})[i].text
    dict["weatherAM"] =  weather[i*3].find('div').find('img')['alt']
    dict["weatherPM"] = weather[i*3 + 1].find('div').find('img')['alt']
    dict["weatherNight"] = weather[i*3 + 2].find('div').find('img')['alt']
    dict["max_tempAM"] = max_temp[i*3].find('span').text 
    dict["max_tempPM"] = max_temp[i*3+1].find('span').text 
    dict["max_tempNight"] = max_temp[i*3+2].find('span').text 
    dict["min_tempAM"] = min_temp[i*3].find('span').text
    dict["min_tempPM"] = min_temp[i*3+1].find('span').text
    dict["min_tempNight"] = min_temp[i*3+2].find('span').text
    dict["humidityAM"] = humidity[i*3].find('span').text
    dict["humidityPM"] = humidity[i*3+1].find('span').text
    dict["humidityNight"] = humidity[i*3+2].find('span').text
    dict["uvAM"] = uv[i*3].find('span').text
    dict["uvPM"] = uv[i*3+1].find('span').text
    dict["uvNight"] = uv[i*3+2].find('span').text
    dict["sunrise"] = sunrise[i*3].find('span').text
    dict["sunset"] = sunset[i*3 + 1].find('span').text 
    
    list.append(dict)
convert = pd.DataFrame(list)
convert.to_csv(f"{city}.csv")
#print(driver.find_elements_by_class_name("b-forecast__table js-forecast-table"))