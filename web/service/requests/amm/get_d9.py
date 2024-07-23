from service.contracts import market_maker
from service.requests.base import abs_class
from users_profile.tasks import *


class GetD9(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        amount = numbers.to_number(validated_data['usdt'], 2)
        self.call = market_maker.MarketMaker(self.keypair)
        self.allowance = self.add_allowances(self.call.contract.contract_address, amount)
        if self.allowance.is_success:
            self.res = self.call.get_d9(amount)
            self.remove_allowances(self.call.contract.contract_address, amount)

    def results(self):
        if self.allowance.is_success:
            update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
            update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address())
            return extractor.get_transfer_data(self.res)
        return self.allowance.extrinsic.value

    def is_success(self):
        if self.allowance.is_success:
            return self.res.is_success
        return False