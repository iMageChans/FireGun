from service.utils import keystone
from service.contracts import usdt
from service.utils.env import config


class Fire:
    def __init__(self, validated_data):
        self.allowances_extrinsice = None
        self.keypair = keystone.check_keypair(validated_data['keypair'])
        self.allowances_extrinsic = usdt.USDT(self.keypair)

    def results(self):
        pass

    def is_success(self):
        pass

    def add_allowances(self, contract: str, amount: int):
        receipt = self.allowances_extrinsic.increase_allowance(contract, amount)
        return receipt

    def remove_allowances(self, contract: str, amount: int):
        receipt = self.allowances_extrinsice.decrease_allowance(contract, amount)
        return receipt
