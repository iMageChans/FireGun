from service.contracts import merchant
from service.requests.base import abs_class
from users_profile.tasks import *


class Redeem(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.redeem_d9()

    def results(self):
        update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        return extractor.get_transfer_data(self.res)

    def is_success(self):
        return self.res.is_success