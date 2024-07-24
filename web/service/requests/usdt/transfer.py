from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from users_profile.tasks import *


class Transfer(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.to_validated_data = validated_data['to_address']
        to_address = get_valid_address(self.to_validated_data)
        value = numbers.to_number(validated_data['value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.transfer(to_address, value)

    def results(self):
        if self.res.is_success:
            update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address())
            update_or_create_usdt_balance_celery.delay(self.to_validated_data)
            return extractor.get_transfer_data(self.res)
        return self.res.error_message

    def is_success(self):
        return self.res.is_success