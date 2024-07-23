from django.core.exceptions import ObjectDoesNotExist

from service.requests.base import abs_class
from service.tools.celery_update_or_create import *

from usdt.serializers import *


class BalanceOf(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            self.usdt_balance = USDTBalance.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            self.usdt_balance = update_or_create_usdt_balance(self.account_id.mate_data_address())

    def results(self):
        if self.usdt_balance is None:
            return None
        return USDTBalanceSerializer(self.usdt_balance).data

    def is_success(self):
        return self.usdt_balance is not None
    #     super().__init__(validated_data)
    #     owner = get_valid_address(validated_data['owner'])
    #     self.call = usdt.USDT(self.keypair)
    #     self.res = self.call.balance_of(owner)
    #
    #     try:
    #         self.usdt_balance = USDTBalance.objects.get(pk=self.account_id.mate_data_address())
    #     except ObjectDoesNotExist:
    #         self.d9_balance = update_or_create_d9_balance(self.account_id.mate_data_address())
    #
    # def results(self):
    #     return numbers.format_number(extractor.get_data_or_err(self.res.value_serialized), 2)
    #
    # def is_success(self):
    #     extractor.get_data_or_err(self.res.value_serialized)
    #     if extractor.check:
    #         return True
    #     return False