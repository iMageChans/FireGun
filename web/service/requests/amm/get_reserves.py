from service.utils import keystone, types
from service.contracts import market_maker
from service.utils import numbers


class GetReserves:
    def __init__(self, validated_data):
        keypair = keystone.check_keypair(validated_data['keypair'])
        self.call = market_maker.MarketMaker(keypair)
        self.res = self.call.get_reserves()

    def results(self):
        values = types.validate_res(self.res.value_serialized)
        keys = ['d9', 'usdt']
        data = dict(zip(keys, values))
        return {
            "d9": "{:.3f}".format(numbers.format_number(data['d9']))[:-1],
            "usdt": "{:.3f}".format(numbers.format_number(data['usdt'], 2))[:-1],
        }

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True

