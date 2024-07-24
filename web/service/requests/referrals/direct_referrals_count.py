from service.pallets import referrals
from service.requests.base import abs_class
from service.utils.json import extractor


class DirectReferralsCount(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = referrals.ReferralsQueries()
        self.res = self.call.direct_referrals_count(self.account_id.get_valid_address())

    def results(self):
        return extractor.get_data_or_err(self.res.value_serialized)

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        if extractor.check:
            return True
        return False