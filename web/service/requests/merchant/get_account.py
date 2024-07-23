from service.contracts import merchant
from service.utils import types
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from service.utils.json import extractor


class GetAccount(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        account_id = get_valid_address(validated_data['account_id'])
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.get_account(account_id)

    def results(self):
        return self.res.value_serialized
        # return {
        #     "provider": extractor.get_data_or_err(self.res.value_serialized)
        # }

    def is_success(self):
        return True
        # extractor.get_data_or_err(self.res.value_serialized)
        # if extractor.check:
        #     return True
        # return False