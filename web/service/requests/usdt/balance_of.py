from service.utils import types
from service.contracts import usdt
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class BalanceOf(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        owner = get_valid_address(validated_data['owner'])
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.balance_of(owner)

    def results(self):
        return types.validate_res(self.res.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.res.value_serialized):
            return False
        return True