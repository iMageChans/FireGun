from django.core.exceptions import ObjectDoesNotExist

from service.requests.base import abs_class
from balances.serializers import D9BalanceSerializer
from service.tools.celery_update_or_create import *


class GetBalance(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            self.d9_balance = D9Balance.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            self.d9_balance = update_or_create_d9_balance(self.account_id.mate_data_address())

    def results(self):
        if self.d9_balance is None:
            return None
        return D9BalanceSerializer(self.d9_balance).data

    def is_success(self):
        return self.d9_balance is not None