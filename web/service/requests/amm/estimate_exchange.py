from service.contracts.base_class import Direction, Currency
from service.utils import keystone, types
from service.contracts import market_maker
from service.utils.numbers import format_number
from service.requests.base import abs_class


class EstimateExchange(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        # direction = Direction(Currency(validated_data['from_currency']).value,
        #                       Currency(validated_data['to_currency']).value)
        # self.from_currency = Currency(validated_data['from_currency'])
        # self.to_currency = Currency(validated_data['to_currency'])
        self.from_amount = validated_data['from_amount']
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.get_reserves()

    def results(self):
        values = types.validate_res(self.res.value_serialized)
        keys = ['d9', 'usdt']
        data = dict(zip(keys, values))
        result = {
            "d9_to_usdt": "{:.7f}".format(format_number(data['usdt'], 2) / format_number(data['d9']) * self.from_amount)[:-1],
            "usdt_to_d9": "{:.7f}".format(format_number(data['d9'] / format_number(data['usdt'], 2) * self.from_amount))[:-1]
        }
        if self.is_success():
            return result
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True