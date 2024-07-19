from service.utils import keystone, types
from service.contracts import market_maker
from service.utils import numbers
from service.utils.accounts import get_valid_address


class GetLiquidityProvider:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            valid_address = get_valid_address(validated_data['account_id'])
        except ValueError as err:
            raise err
        res = market_maker.MarketMaker(keypair).get_liquidity_provider(valid_address).value
        values = types.validate_res(res)
        self.values = values


    def results(self):
        return {
            "data": self.values
        }