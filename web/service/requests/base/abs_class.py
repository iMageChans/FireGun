from service.utils import keystone
from service.contracts import usdt


class Fire:
    def __init__(self, validated_data):
        self.keypair = keystone.check_keypair(validated_data['keypair'])

    def results(self):
        pass

    def is_success(self):
        pass

    def add_allowances(self, contract: str, amount: int):
        usdt.USDT(self.keypair).increase_allowance(contract, amount)

    def remove_allowances(self, contract: str, amount: int):
        usdt.USDT(self.keypair).decrease_allowance(contract, amount)
