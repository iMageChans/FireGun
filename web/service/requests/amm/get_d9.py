from service.utils import types
from service.contracts import market_maker
from service.utils import numbers
from service.requests.base import abs_class


class GetD9(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        amount = numbers.to_number(validated_data['usdt'], 2)
        self.call = market_maker.MarketMaker(self.keypair)
        allowance = self.add_allowances(self.call.contract.contract_address, amount)
        if allowance.is_success:
            self.res = self.call.get_d9(amount)
            self.remove_allowances(self.call.contract.contract_address, amount)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True