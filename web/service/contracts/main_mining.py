from service.contracts.base_class import D9Contract
from substrateinterface import Keypair


class MainMining(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('MAIN_MINING_CONTRACT', 'main_pool.json', keypair)

    def burn(self, burn_beneficiary: str, burn_contract: str, burn_amount: int):
        params = {
            "burn_beneficiary": burn_beneficiary,
            "burn_contract": burn_contract
        }
        return self.contract_exec('burn', params, value=burn_amount)

    def withdraw(self, burn_contract: str):
        params = {
            "burn_contract": burn_contract,
        }
        self.contract_exec('withdraw', params)

    def get_ancestors(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_exec('get_ancestors', params)

    def get_total_burned(self):
        return self.contract_read('get_total_burned')
