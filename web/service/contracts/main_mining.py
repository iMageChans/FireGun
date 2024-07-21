from service.contracts.base_class import D9Contract, config
from substrateinterface import Keypair


class MainMining(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('MAIN_MINING_CONTRACT', 'main_pool.json', keypair)

    def burn(self, burn_beneficiary: str, burn_amount: int):
        params = {
            "burn_beneficiary": burn_beneficiary,
            "burn_contract": config.get('BURN_MINING_CONTRACT')
        }
        return self.contract_exec('burn', params, value=burn_amount)

    def withdraw(self):
        params = {
            "burn_contract": config.get('BURN_MINING_CONTRACT'),
        }
        return self.contract_exec('withdraw', params)

    def get_ancestors(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_ancestors', params)

    def get_total_burned(self):
        return self.contract_read('get_total_burned')

    def get_portfolio(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_read('get_portfolio', params)
