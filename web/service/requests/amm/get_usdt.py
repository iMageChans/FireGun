from service.contracts import market_maker
from service.requests.base import abs_class
from users_profile.tasks import *


class GetUSDT(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        d9_amount = numbers.to_number(validated_data['d9_amount'])
        self.call = market_maker.MarketMaker(self.keypair)
        self.res = self.call.get_usdt(d9_amount)

    def results(self):
        update_or_create_d9_balance_celery.delay(self.account_id.mate_data_address())
        update_or_create_usdt_balance_celery.delay(self.account_id.mate_data_address())
        return extractor.get_transfer_data(self.res)

    def is_success(self):
        return self.res.is_success