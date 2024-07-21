from service.utils import keystone
from service.pallets import balances
from service.utils.accounts import get_valid_address
from service.utils import numbers


class GetBalance:
    def __init__(self, validated_data):
        try:
            self.keypair = keystone.check_keypair(validated_data['keypair'])
            self.valid_address = get_valid_address(validated_data['account_id'])
        except ValueError as err:
            self.valid_address = self.keypair.ss58_address
            raise err
        self.res = balances.BalancesQueries().get_balance(self.valid_address)

    def results(self):
        return {
            "data": "{:.5f}".format(numbers.format_number(self.res))[:-1]
        }