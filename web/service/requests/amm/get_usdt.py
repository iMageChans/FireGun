from service.utils import types
from service.contracts import market_maker
from service.utils import numbers
from service.requests.base import abs_class


class GetUSDT(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        d9_amount = numbers.to_number(validated_data['d9_amount'])
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.get_usdt(d9_amount)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True