import requests
import json
from config import currencies


# Один из вариантов самописной функции, которая позволяет сокращать количество знаков после запятой, на случай,
# если не хочется пользоваться, по каким-то причинам, format(x, '.xf').
#  def toFixed(numObj, digits=0):
#      return f"{numObj:.{digits}f}"

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = currencies[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Некорректный формат суммы {amount}!\nОбратитесь к /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[currencies[base]]) * amount
        return format(total_base, '.2f')
