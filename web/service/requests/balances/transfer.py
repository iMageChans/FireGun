from service.utils import keystone
from service.pallets import balances
from service.utils.accounts import get_valid_address
from service.utils import numbers


class Transfer:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            valid_address = get_valid_address(validated_data['to_address'])
            amount = numbers.to_number(validated_data['amount'])
        except ValueError as err:
            raise err
        call = balances.BalancesExtrinsics().transfer(valid_address, amount)
        nonce = balances.BalancesExtrinsics().chain_interface.query('System', 'Account', [keypair.ss58_address])
        extrinsic = balances.BalancesExtrinsics().chain_interface.create_signed_extrinsic(call=call, keypair=keypair, nonce=nonce.value['nonce'])
        self.res = balances.BalancesExtrinsics().chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)

    def results(self):
        return self.res