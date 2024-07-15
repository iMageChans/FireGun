from service.contracts.base_class import D9Contract
from substrateinterface import Keypair


class Merchant(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('MERCHANT_CONTRACT', 'd9_merchant_mining.json', keypair)

    def subscribe(self, account_id: str, usdt_base_units: int):
        params = {
            "usdt_amount": usdt_base_units,
        }
        return self.contract_exec('subscribe', params, usdt_base_units)

    def redeem_d9(self):
        return self.contract_read('redeem_d9')

    def give_points_d9(self, consumer_id: str, d9_amount: int):
        params = {
            "consumer_id": consumer_id,
        }
        return self.contract_exec('give_points_d9', params, value=d9_amount)

    def give_points_usdt(self, consumer_id: str, usdt_amount: int):
        params = {
            "consumer_id": consumer_id,
            "usdt_payment": usdt_amount
        }
        return self.contract_exec('give_points_usdt', params, value=usdt_amount)

    def send_usdt_payment_to_merchant(self, merchant_id: str, usdt_amount: int):
        params = {
            "merchant_id": merchant_id,
            "usdt_payment": usdt_amount
        }
        return self.contract_exec('send_usdt_payment_to_merchant', params, value=usdt_amount)

    def send_d9_payment_to_merchant(self, merchant_id: str, d9_amount: int):
        params = {
            "merchant_id": merchant_id,
        }
        return self.contract_exec('send_d9_payment_to_merchant', params, value=d9_amount)

    def get_merchant_expiry(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_exec('get_expiry', params)

    def get_account(self, account_id: str):
        params = {
            "account_id": account_id,
        }
        return self.contract_exec('get_account', params)