from service.pallets import balances
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class


class GetLocks(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.valid_address = get_valid_address(validated_data['account_id'])
        self.call = balances.BalancesQueries()
        self.res = self.call.get_locks(self.valid_address)

    def results(self):
        return self.res.value_serialized['data']

    def is_success(self):
        if "Err" in self.res.value_serialized['data']:
            return False
        return True