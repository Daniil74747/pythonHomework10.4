import sqlite3
import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect('weather.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather_Dnipro(date_time TEXT, temperature REAL)''')

response = requests.get('https://sinoptik.ua/')
soup = BeautifulSoup(response.text, 'html.parser')

temperature = soup.find(name='tr', class_='temperature').text
date_time = soup.find(name='tr', class_='gray time').text

tables = (date_time, temperature)
print(tables)

Dates = ('3:00', '+15')
c.execute("INSERT INTO weather_Dnipro (date_time, temperature) VALUES ('0:00', +16)")
weather = ('3:00', +15)
c.execute("INSERT INTO weather_Dnipro (date_time, temperature) VALUES (?, ?)", weather)

weathers = [('6:00', +17), ('9:00', +20), ('12:00', +19)]
c.executemany("INSERT INTO weather_Dnipro (date_time, temperature) VALUES (?, ?)", weathers)


conn.commit()
conn.close()
