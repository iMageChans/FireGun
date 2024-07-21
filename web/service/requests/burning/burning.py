from service.utils import keystone
from service.contracts import main_mining
from service.utils import numbers
from service.utils.accounts import get_valid_address
from service.utils import types


class Token:
    def __init__(self, validated_data):
        keypair = keystone.check_keypair(validated_data['keypair'])
        account_id = get_valid_address(validated_data['account_id'])
        amount = numbers.to_number(validated_data['amount'])
        self.call = main_mining.MainMining(keypair)
        self.res = self.call.burn(burn_beneficiary=account_id, burn_amount=amount)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True