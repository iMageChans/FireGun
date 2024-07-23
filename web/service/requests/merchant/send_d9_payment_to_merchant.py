from service.contracts import merchant
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from users_profile.tasks import *


class D9Payment(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        merchant_id = get_valid_address(validated_data['merchant_id'])
        d9_amount = numbers.to_number(validated_data['d9_amount'])
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.send_d9_payment_to_merchant(merchant_id, d9_amount)

    def results(self):
        update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        return extractor.get_transfer_data(self.res)

    def is_success(self):
        return self.res.is_success