import requests
import json

# отримуємо координати міста
city_name = input("Введіть назву міста: ")
url = f"https://api.open-meteo.com/v1/place?q={city_name.replace(' ', '+')}"
response = requests.get(url)
if response.status_code != 200:
    print(f"Помилка отримання координат міста: {response.status_code}")
    exit()

data = json.loads(response.text)
if len(data) == 0:
    print(f"Місто {city_name} не знайдене")
    exit()

lat, lon = data[0]['latitude'], data[0]['longitude']

# отримуємо погоду за координатами міста
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
response = requests.get(url)
if response.status_code != 200:
    print(f"Помилка отримання погодних даних: {response.status_code}")
    exit()

data = json.loads(response.text)

# виводимо результати
print(f"Погода в місті {city_name}:")
print(f"Температура: {data['temperature']['value']}°C")
print(f"Атмосферний тиск: {data['pressure_sea_level']['value']} гПа")
print(f"Вологість: {data['humidity']['value']}%")
