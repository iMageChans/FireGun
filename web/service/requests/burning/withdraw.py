from service.utils import keystone
from service.contracts import main_mining
from service.utils import types
from service.requests.base import abs_class


class Withdraw(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = main_mining.MainMining(self.keypair)
        self.res = self.call.withdraw()

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        return self.res.is_success