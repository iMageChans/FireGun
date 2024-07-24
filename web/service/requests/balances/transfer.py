from service.utils.accounts import get_valid_address
from service.requests.base import abs_class
from users_profile.tasks import *


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
        if self.res.is_success:
            update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
            return extractor.get_transfer_data(self.res)
        return self.res.error_message

    def is_success(self):
        return self.res.is_success