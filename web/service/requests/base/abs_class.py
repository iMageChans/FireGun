from service.utils import keystone
from service.contracts import usdt


class Fire:
    def __init__(self, validated_data):
        self.add = None
        self.remove = None
        self.keypair = keystone.check_keypair(validated_data['keypair'])

    def results(self):
        pass

    def is_success(self):
        pass

    def add_allowances(self, contract: str, amount: int):
        self.add = usdt.USDT(self.keypair)
        receipt = self.add.increase_allowance(contract, amount)
        return receipt

    def remove_allowances(self, contract: str, amount: int):
        self.remove = usdt.USDT(self.keypair)
        receipt = self.remove.decrease_allowance(contract, amount)
        return receipt
