from service.utils import types
from service.contracts import usdt
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from service.utils.json import extractor


class Approve(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)

        spender = get_valid_address(validated_data['spender'])
        value = numbers.to_number(validated_data['value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.approve(spender, value)

    def results(self):
        return {
            "provider": extractor.get_data_or_err(self.res.value_serialized)
        }

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        if extractor.check:
            return True
        return False