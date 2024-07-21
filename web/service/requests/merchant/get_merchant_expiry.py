from service.contracts import merchant
from service.utils import types
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class GetMerchantExpiry(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        account_id = get_valid_address(validated_data['account_id'])
        self.call = merchant.Merchant(self.keypair)
        self.res = self.call.get_merchant_expiry(account_id)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True