import requests
import random

sites = ['http://google.com', 'http://facebook.com', 'http://twitter.com', 'http://amazon.com', 'http://apple.com']

# організуємо випадковий вибір сайту
site = random.choice(sites)

# здійснюємо запит
response = requests.get(site)

# Виведем результат:
print(f"Сайт: {site}")
print(f"Статус-код відповіді: {response.status_code}")
print(f"Довжина HTML-коду: {len(response.text)}")