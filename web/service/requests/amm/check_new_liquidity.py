from service.contracts import market_maker
from service.requests.base import abs_class
from service.utils.json import extractor


class CheckNewLiquidity(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_liquidity = validated_data['usdt_liquidity']
        d9_liquidity = validated_data['d9_liquidity']
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.check_new_liquidity(usdt_liquidity, d9_liquidity)

    def results(self):
        values = extractor.get_data_or_err(self.res.value_serialized)
        return values

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        return extractor.check