from service.utils import types
from service.contracts import usdt
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from service.utils.json import extractor


class DecreaseAllowance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        spender = get_valid_address(validated_data['spender'])
        delta_value = numbers.to_number(validated_data['delta_value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.decrease_allowance(spender, delta_value)

    def results(self):
        if self.res.is_success:
            return extractor.get_transfer_data(self.res)
        return self.res.error_message

    def is_success(self):
        return self.res.is_success