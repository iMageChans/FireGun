from service.contracts.base_class import D9Contract, Direction
from substrateinterface import Keypair


class MarketMaker(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('MARKET_MAKER_CONTRACT', 'market_maker.json', keypair)

    def get_reserves(self):
        return self.contract_read('get_currency_reserves')

    def get_liquidity_provider(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_exec('get_liquidity_provider', params)

    def add_liquidity(self, usdt_amount: int, d9_amount: int):
        params = {
            "usdt_liquidity": usdt_amount,
        }
        return self.contract_exec('add_liquidity', params, value=d9_amount)

    def remove_liquidity(self):
        return self.contract_read('remove_liquidity')

    def check_new_liquidity(self, usdt_liquidity: int, d9_liquidity: int):
        params = {
            "usdt_liquidity": usdt_liquidity,
            "d9_liquidity": d9_liquidity
        }
        return self.contract_exec('check_new_liquidity', params)

    def get_d9(self, usdt: int):
        params = {
            "usdt": usdt
        }
        return self.contract_exec('get_d9', params)

    def get_usdt(self, d9_amount: int):
        return self.contract_exec('get_usdt', value=d9_amount)

    def calculate_exchange(self, direction: Direction, from_amount: int):
        params = {
            "direction": direction,
            "amount_0": from_amount
        }
        return self.contract_exec('calculate_exchange', params)

    def estimate_exchange(self, direction: Direction, from_amount: int):
        params = {
            "direction": direction,
            "amount_0": from_amount
        }
        return self.contract_exec('estimate_exchange', params)

    def check_usdt_balance(self, account_id: str, usdt_amount: int):
        params = {
            "account_id": account_id,
            "amount": usdt_amount
        }
        return self.contract_exec('check_usdt_balance', params)