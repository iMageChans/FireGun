from service.utils import types
from service.contracts import usdt
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class TransferFrom(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        from_address = get_valid_address(validated_data['from_address'])
        to_address = get_valid_address(validated_data['to_address'])
        value = numbers.to_number(validated_data['value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.transfer_from(from_address, to_address, value)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True