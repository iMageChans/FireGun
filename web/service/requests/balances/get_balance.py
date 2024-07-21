from service.pallets import balances
from service.utils.accounts import get_valid_address
from service.utils import numbers
from service.requests.base import abs_class


class GetBalance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.valid_address = get_valid_address(validated_data['account_id'])
        self.call = balances.BalancesQueries()
        self.res = self.call.get_balance(self.valid_address)

    def results(self):
        value = self.res.value_serialized['data']['free']
        if self.is_success():
            return {
                "totals": "{:.5f}".format(numbers.format_number(value))[:-1]
            }
        return self.res.value_serialized['data']

    def is_success(self):
        if "Err" in self.res.value_serialized['data']:
            return False
        return True