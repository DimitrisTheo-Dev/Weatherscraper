import requests
import pandas as pd
from bs4 import BeautifulSoup
#In pages i can change states
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.33865000000003&lon=-121.88541999999995#.Xm_tnZMzZo4')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')
#print(items)

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())
period_names = [item.find(class_='period-name').get_text()for item in items]
short_desc = [item.find(class_='short-desc').get_text()for item in items]
temp = [item.find(class_='temp').get_text()for item in items]
#print(period_names)
#print(short_desc)
#print(temp)
weather = pd.DataFrame(
    { 'period': period_names,
      'short-description': short_desc,
      'temperatures': temp,
      }
)
print(weather)
weather.to_csv('weather.csv')