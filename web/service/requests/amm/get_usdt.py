from service.utils import keystone
from service.contracts import market_maker
from service.utils import numbers


class GetUSDT:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            d9_amount = numbers.to_number(validated_data['d9_amount'])
        except ValueError as err:
            raise err
        self.res = market_maker.MarketMaker(keypair).get_usdt(d9_amount)

    def results(self):
        return self.res