from amm.models import CurrencyReserves
from service.utils import keystone
from service.utils.json import extractor
from service.contracts import market_maker
from service.utils import numbers


class GetReserves:
    def __init__(self, validated_data):
        res = market_maker.MarketMaker(validated_data['keypair'])

    def results(self):
        first_currency_reserve = CurrencyReserves.objects.first()
        return {
            "d9": "{:.3f}".format(numbers.format_number(first_currency_reserve.d9))[:-1],
            "usdt": "{:.3f}".format(numbers.format_number(first_currency_reserve.usdt, 2))[:-1],
        }

    def is_success(self):
        first_currency_reserve = CurrencyReserves.objects.first()
        if first_currency_reserve is not None:
            return True
        return False

