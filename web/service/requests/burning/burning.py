from service.contracts import main_mining
from service.utils import numbers
from service.utils.accounts import get_valid_address
from service.utils import types
from service.requests.base import abs_class


class Token(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        account_id = get_valid_address(validated_data['account_id'])
        amount = numbers.to_number(validated_data['amount'])
        self.call = main_mining.MainMining(self.keypair)
        self.res = self.call.burn(burn_beneficiary=account_id, burn_amount=amount)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True