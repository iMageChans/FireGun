from service.utils import keystone, types
from service.contracts import market_maker
from service.requests.base import abs_class


class RemoveLiquidity(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.remove_liquidity()

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True