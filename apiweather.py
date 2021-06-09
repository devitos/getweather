import requests
from urllib.parse import urljoin
from pprint import pprint


def get_weather():
    city_name = 'Saint Petersburg, RU'
    API_KEY = ''  # Вставьте сюда свой API-ключ
    API_FIND_URL = 'http://api.openweathermap.org/data/2.5/find'
    API_GET_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/onecall'

    resp = requests.get(API_FIND_URL, params={'q': city_name, 'units': 'metric', 'APPID': API_KEY})
    city_list = resp.json()
    city_id = city_list['list'][0]['id']
    coord_lat = city_list['list'][0]['coord']['lat']
    coord_lon = city_list['list'][0]['coord']['lon']
    resp_weather = requests.get(API_GET_WEATHER_URL, params={'lat': coord_lat, 'lon': coord_lon, 'units': 'metric',
                                                             'lang': 'ru', 'exclude': 'current,minutely,hourly',
                                                             'appid': API_KEY})
    answer = resp_weather.json()
    five_day = answer['daily'][0:5]
    max_pressure = 0
    max_temp_dif = 0
    for day in five_day:
        temp_dif = day['temp']['day'] - day['temp']['night']
        if day['pressure'] > max_pressure:
            max_pressure = day['pressure']
        if temp_dif > max_temp_dif:
            max_temp_dif = temp_dif

    print(f'Город {city_name} находится по координатам {coord_lat} : {coord_lat} . ID по базе = {city_id} ')
    print(f'Максимальное давление равно {max_pressure} hPA')
    print(f'Максимальная разница темпенратур равна {round(max_temp_dif, 2)}')
    return


if __name__ == '__main__':
    get_weather()
