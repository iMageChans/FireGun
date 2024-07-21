from service.contracts.base_class import D9Contract
from substrateinterface import Keypair


class BurnMining(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('BURN_MINING_CONTRACT', 'd9_burn_mining.json', keypair)

    def get_return_percent(self):
        return self.contract_read('get_return_percent')