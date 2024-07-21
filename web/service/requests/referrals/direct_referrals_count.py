from service.pallets import referrals
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class


class DirectReferralsCount(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.valid_address = get_valid_address(validated_data['account_id'])
        self.call = referrals.ReferralsQueries()
        self.res = self.call.direct_referrals_count(self.valid_address)

    def results(self):
        return self.res.value_serialized

    def is_success(self):
        if "Err" in self.res.value_serialized:
            return False
        return True