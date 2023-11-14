import json
import os
from datetime import datetime

import requests

API_KEY = os.getenv('API')
CURRENCY_RATES_FILE = 'currency_rates.json'
# API = 'VAXraUnYGcaknD6mkhNw5o8sY2TIF69G'


def main():
    while True:
        currency = input('Введите название валюты (USD po EUR)\n-> ').upper()
        if currency not in ('USD', 'EUR'):
            print('не корректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choise = input('Выберите действия (1 - продолжить, 2 - выйти)\n-> ')
        if choise == '1':
            continue
        elif choise == '2':
            break
        else:
            print('Не корректный ввод')


def get_currency_rate(base):
    """ Получаем курс от API и возвращает его в виде float"""
    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, headers=headers, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data):
    """Сохраняет данные в JSON-файл"""

    with open(CURRENCY_RATES_FILE, 'a', encoding='utf-8') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as json_file:
                data_list = json.load(json_file)
            data_list.append(data)
            with open(CURRENCY_RATES_FILE, "w") as json_file:
                json.dump(data_list, json_file)


if __name__ == '__main__':
    main()
