import requests
import sqlite3


print("EXTRACT: Adatok letöltése")
url = "https://api.open-meteo.com/v1/forecast?latitude=47.53&longitude=21.62&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
response.raise_for_status() 
weather_data = response.json()




print("TRANSFORM: Adatok tisztítása")
hourly_data = weather_data.get('hourly', {})
times = hourly_data.get('time', [])
temps = hourly_data.get('temperature_2m', [])
humidity = hourly_data.get('relative_humidity_2m', [])
wind = hourly_data.get('wind_speed_10m', [])

clean_data = []

for time, temp, hum, wnd in zip(times, temps, humidity, wind):
    if temp > 15:
        clean_data.append({
        'time': time,
        'temperature': temp,
        'humidity': hum,
        'wind_speed': wnd,
        'place': 'Debrecen'
    })
        


print("LOAD: Adatok mentése adatbázisba")

conn = sqlite3.connect('weather.db')
cursor = conn.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS debrecen_weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    temperature REAL,
    humidity integer,
    wind_speed REAL,
    place TEXT
)''')

cursor.execute('DELETE FROM debrecen_idojaras')

for entry in clean_data:
    cursor.execute('''INSERT INTO debrecen_weather (time, temperature, humidity, wind_speed, place)
                      VALUES (?, ?, ?, ?, ?)''',
                   (entry['time'], entry['temperature'], entry['humidity'], entry['wind_speed'], entry['place']))

conn.commit()
conn.close()

