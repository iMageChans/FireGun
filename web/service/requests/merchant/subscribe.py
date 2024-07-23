from service.contracts import merchant
from service.requests.base import abs_class
from users_profile.tasks import *


class Subscribe(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_base_units = validated_data['usdt_base_units']
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.subscribe(usdt_base_units)

    def results(self):
        update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address())
        return extractor.get_transfer_data(self.res)

    def is_success(self):
        return self.res.is_success