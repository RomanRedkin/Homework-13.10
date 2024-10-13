import requests
# Імпортуємо бібліоткету Requests, котра дозволяє відправляти запроси на Python
from .read_json import read_json
# Імпортуємо функцію "read_json" з пакету json файлу
import json
# Імпортуємо модуль "json", який дозволяє працювати з json даними
data_api = read_json(name_file= 'config_api.json')
# Викликаємо функцію "read_json", щоб прочитати файл "config_api.json", збереження даних у "data_api"
API_KEY = data_api['api_key']
# Отримуємо API ключ з json файлу та зберігаємо його у змінну "API_KEY"
CITY_NAME = data_api['city_name']
# Отримуємо назву нашого міста з json файлу та зберігаємо його у змінну "CITY_NAME"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
# Робимо URL для запиту до API (OpenWeatherMap), використовуючи нашу назву міста і API ключ
response = requests.get(URL)
# Робимо запит до OpenWeatherMap API за створенною URL адресою і записуємо відповідь у змінну "response"
if response.status_code == 200:
    # Зробимо перевірку, якщо статус відповіді дорівнює 200 то це значить, що запит успішний
    data_dict = json.loads(response.content)
    # Завантажуємо отримані дані у форматі json (перетворюємо їх на словник) в змінну "data_dict" 
    print(json.dumps(data_dict, indent= 4))