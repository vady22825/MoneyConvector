import json
import requests
from config import keys

class ConvertionExeption(Exception):
    pass

class MoneyConvertion:
    @staticmethod
    def convert(quote:str, base:str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые купюры {base}')

        try:
            quote_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Неудалось обработать валюту {base}')

        try:
            base_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Неудалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
