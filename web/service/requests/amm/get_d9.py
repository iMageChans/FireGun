from substrateinterface.exceptions import ContractReadFailedException

from service.utils import keystone
from service.contracts import market_maker, usdt
from service.utils import numbers


class GetD9:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            amount = numbers.to_number(validated_data['usdt'], 2)
        except ValueError as err:
            raise err

        try:
            approve = usdt.USDT(keypair).approve(keypair.ss58_address, amount)
            print(approve.is_success)
            allowance = usdt.USDT(keypair).increase_allowance(keypair.ss58_address, amount)
            print(allowance.is_success)
            self.res = market_maker.MarketMaker(keypair).get_d9(amount)
            print(self.res.is_success)
            # print("error_message:", self.res.error_message.values()[3])
            # print("extrinsic", self.res.extrinsic)
            # print(self.res.is_success)
            # print(self.res.total_fee_amount)
            # print(self.res.contract_events)
            # print(self.res.triggered_events)
            # print(self.res.substrate.block_hash)
        except Exception as err:
            print(err)

    def results(self):
        return self.res