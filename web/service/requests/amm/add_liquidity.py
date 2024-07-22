from service.utils import types
from service.contracts import market_maker
from service.utils import numbers
from service.requests.base import abs_class
from service.utils.env import config


class AddLiquidity(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        usdt_amount = numbers.to_number(validated_data['usdt_amount'], 2)
        d9_amount = numbers.to_number(validated_data['d9_amount'])
        self.call = market_maker.MarketMaker(self.keypair)
        self.add_allowances(self.call.contract.contract_address, usdt_amount)
        self.add_allowances(config.get('USDT_CONTRACT'), usdt_amount)
        print("USDT_CONTRACT:", config.get('USDT_CONTRACT'))
        print("AMM_CONTRACT:", self.call.contract.contract_address)
        self.res = self.call.add_liquidity(usdt_amount=usdt_amount, d9_amount=d9_amount)

    def results(self):
        return self.call.gas_predit_result.value_serialized

    def is_success(self):
        print(self.res.is_success)
        return self.res.is_success
