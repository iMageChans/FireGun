from service.contracts import merchant
from service.utils import types, numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class D9Payment(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        merchant_id = get_valid_address(validated_data['merchant_id'])
        d9_amount = numbers.to_number(validated_data['d9_amount'])
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.send_d9_payment_to_merchant(merchant_id, d9_amount)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True