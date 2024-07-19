from service.utils import keystone, types
from service.contracts import market_maker
from service.utils import numbers


class RemoveLiquidity:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
        except ValueError as err:
            raise err
        self.res = market_maker.MarketMaker(keypair).remove_liquidity()

    def results(self):
        return self.res