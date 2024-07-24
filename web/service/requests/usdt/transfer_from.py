from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from users_profile.tasks import *


class TransferFrom(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.from_validated_data = validated_data['from_address']
        self.to_validated_data = validated_data['to_address']
        from_address = get_valid_address(self.to_validated_data)
        to_address = get_valid_address(validated_data['to_address'])
        value = numbers.to_number(validated_data['value'], 2)
        self.call = usdt.USDT(self.keypair)
        self.res = self.call.transfer_from(from_address, to_address, value)

    def results(self):
        if self.res.is_success:
            update_or_create_usdt_balance_celery.delay(self.from_validated_data)
            update_or_create_usdt_balance_celery.delay(self.to_validated_data)
            return extractor.get_transfer_data(self.res)
        return self.res.error_message

    def is_success(self):
        return self.res.is_success