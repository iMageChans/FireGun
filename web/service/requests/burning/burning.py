from service.requests.base import abs_class
from users_profile.tasks import *


class Token(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        amount = numbers.to_number(validated_data['amount'])
        self.call = main_mining.MainMining(self.keypair)
        self.res = self.call.burn(burn_beneficiary=self.account_id.get_valid_address(), burn_amount=amount)

    def results(self):
        if self.res.is_success:

            update_or_create_user_burning_profile_celery.delay(self.account_id.mate_data_address())
            update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())

            return extractor.get_transfer_data(self.res)
        return self.call.gas_predit_result.value_serialized

    def is_success(self):
        return self.res.is_success