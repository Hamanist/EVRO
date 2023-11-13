import os
from datetime import datetime


def main():
    while True:
        currency = input('Введите название валюты (USD po EUR)\n-> ')
        if currency not in ('USD', 'EUR'):
            print('не корректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choise = input('Выберите действия (1 - продолжить, 2 - выйти)\n->')
        if choise == '1':
            continue
        elif choise == '2':
            break
        else:
            print('Не корректный ввод')


def get_currency_rate(base): ...


def save_to_json(data): ...


if __name__ == '__main__':
    main()
