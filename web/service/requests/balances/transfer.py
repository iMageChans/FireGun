from service.utils import keystone
from service.pallets import balances
from service.utils.accounts import get_valid_address
from service.utils import numbers
from service.requests.base import abs_class


class Transfer(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        valid_address = get_valid_address(validated_data['to_address'])
        amount = numbers.to_number(validated_data['amount'])
        call = balances.BalancesExtrinsics().transfer(valid_address, amount)
        nonce = balances.BalancesExtrinsics().chain_interface.query('System', 'Account', [self.keypair.ss58_address])
        self.extrinsic = balances.BalancesExtrinsics().chain_interface.create_signed_extrinsic(call=call, keypair=self.keypair, nonce=nonce.value['nonce'])
        self.res = balances.BalancesExtrinsics().chain_interface.submit_extrinsic(self.extrinsic, wait_for_inclusion=True)

    def results(self):
        return self.res.extrinsic.value_serialized

    def is_success(self):
        return self.res.is_success