from service.utils import types
from service.contracts import market_maker
from service.utils.accounts import get_valid_address
from service.utils import numbers
from service.requests.base import abs_class


class CheckUSDTBalance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['account_id'])
        amount = numbers.to_number(validated_data['amount'], 2)
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.check_usdt_balance(valid_address, amount)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True