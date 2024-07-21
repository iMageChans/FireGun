from service.contracts import merchant
from service.utils import types, numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class GivePointsUSDT(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        consumer_id = get_valid_address(validated_data['consumer_id'])
        usdt_amount = numbers.to_number(validated_data['usdt_amount'], 2)
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.give_points_usdt(consumer_id, usdt_amount)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True