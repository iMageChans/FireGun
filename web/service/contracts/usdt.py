from service.contracts.base_class import D9Contract
from substrateinterface import Keypair


class USDT(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('USDT_CONTRACT', 'd9_usdt.json', keypair)

    def approve(self, spender: str, amount: int):
        params = {
            "spender": spender,
            "value": amount
        }
        return self.contract_exec('psp22::approve', params)

    def decrease_allowance(self, spender: str, delta_value: int):
        params = {
            "spender": spender,
            "delta_value": delta_value
        }
        return self.contract_exec('psp22::decrease_allowance', params)

    def increase_allowance(self, spender: str, delta_value: int):
        params = {
            "spender": spender,
            "delta_value": delta_value
        }
        return self.contract_exec('psp22::increase_allowance', params)

    def transfer(self, to: str, value: int):
        params = {
            "to": to,
            "value": value,
            "data": "0x"
        }
        return self.contract_exec('psp22::transfer', params)

    def transfer_from(self, from_: str, to: str, value: int):
        params = {
            "from": from_,
            "to": to,
            "value": value,
            "data": "0x"
        }
        return self.contract_exec('psp22::transfer_from', params)

    def balance_of(self, owner: str):
        return self.contract_exec('psp22::balance_of', {'owner': owner})

    def total_supply(self):
        return self.contract_read('psp22::total_supply')