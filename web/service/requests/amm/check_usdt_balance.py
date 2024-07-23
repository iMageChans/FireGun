from service.contracts import market_maker
from service.utils.accounts import get_valid_address
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.json import extractor


class CheckUSDTBalance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['account_id'])
        amount = numbers.to_number(validated_data['amount'], 2)
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.check_usdt_balance(valid_address, amount)

    def results(self):
        values = extractor.get_data_or_err(self.res.value_serialized)
        return values

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        return extractor.check