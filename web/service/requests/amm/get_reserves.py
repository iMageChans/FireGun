from service.utils import keystone, types
from service.contracts import market_maker
from service.utils import numbers


class GetReserves:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
        except ValueError as err:
            raise err
        res = market_maker.MarketMaker(keypair).get_reserves().value
        values = types.validate_res(res)
        keys = ['d9', 'usdt']
        data = dict(zip(keys, values))
        self.d9 = data['d9']
        self.usdt = data['usdt']

    def results(self):
        return {
            "d9": "{:.3f}".format(numbers.format_number(self.d9))[:-1],
            "usdt": "{:.3f}".format(numbers.format_number(self.usdt, 2))[:-1],
        }

