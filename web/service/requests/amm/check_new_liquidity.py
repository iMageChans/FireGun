from service.utils import types
from service.contracts import market_maker
from service.requests.base import abs_class


class CheckNewLiquidity(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_liquidity = validated_data['usdt_liquidity']
        d9_liquidity = validated_data['d9_liquidity']
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.check_new_liquidity(usdt_liquidity, d9_liquidity)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True