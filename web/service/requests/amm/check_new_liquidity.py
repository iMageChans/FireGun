from service.utils import keystone
from service.contracts import market_maker


class CheckNewLiquidity:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            usdt_liquidity = validated_data['usdt_liquidity']
            d9_liquidity = validated_data['d9_liquidity']
        except ValueError as err:
            raise err
        self.res = market_maker.MarketMaker(keypair).check_new_liquidity(usdt_liquidity, d9_liquidity)

    def results(self):
        return self.res