from service.contracts import main_mining
from service.requests.base import abs_class
from users_profile.tasks import *


class Withdraw(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = main_mining.MainMining(self.keypair)
        self.res = self.call.withdraw()

    def results(self):
        if self.res.is_success:
            try:
                update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
                update_or_create_user_burning_profile_celery.delay(self.account_id.mate_data_address())
            except Exception as e:
                return e
            return extractor.get_transfer_data(self.res)

    def is_success(self):
        return self.res.is_success