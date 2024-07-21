from service.contracts import market_maker
from service.utils import numbers
from service.requests.base import abs_class


class GetD9(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        amount = numbers.to_number(validated_data['usdt'], 2)
        self.call = market_maker.MarketMaker(self.keypair)
        self.allowance = self.add_allowances(self.call.contract.contract_address, amount)
        if self.allowance.is_success:
            self.res = self.call.get_d9(amount)
            self.remove_allowances(self.call.contract.contract_address, amount)

    def results(self):
        if self.allowance.is_success:
            return self.call.gas_predit_result.value_serialized
        return self.allowance.extrinsic.value

    def is_success(self):
        if self.allowance.is_success:
            return self.res.is_success
        return False