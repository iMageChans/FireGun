from service.contracts import merchant
from service.utils import numbers
from service.utils.accounts import get_valid_address
from service.utils import types
from service.requests.base import abs_class


class Subscribe(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_base_units = validated_data['usdt_base_units']
        # amount = numbers.to_number(validated_data['amount'])
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.subscribe(usdt_base_units)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True