from service.contracts import market_maker
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class
from service.utils.json import extractor


class GetLiquidityProvider(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['account_id'])
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.get_liquidity_provider(valid_address)

    def results(self):
        return {
            "provider": extractor.get_data_or_err(self.res.value_serialized)
        }

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        return extractor.check