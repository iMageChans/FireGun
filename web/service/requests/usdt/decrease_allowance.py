from service.utils import types
from service.contracts import usdt
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class DecreaseAllowance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        spender = get_valid_address(validated_data['spender'])
        delta_value = numbers.to_number(validated_data['delta_value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.decrease_allowance(spender, delta_value)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True