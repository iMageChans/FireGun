from service.utils import keystone, types
from service.contracts import market_maker
from service.utils import numbers
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class


class GetLiquidityProvider(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['account_id'])
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.get_liquidity_provider(valid_address)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True