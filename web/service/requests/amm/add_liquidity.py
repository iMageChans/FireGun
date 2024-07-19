from service.utils import keystone
from service.contracts import market_maker


class AddLiquidity:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            usdt_amount = validated_data['usdt_amount']
            d9_amount = validated_data['d9_amount']
        except ValueError as err:
            raise err
        self.res = market_maker.MarketMaker(keypair).add_liquidity(usdt_amount, d9_amount)

    def results(self):
        return self.res
