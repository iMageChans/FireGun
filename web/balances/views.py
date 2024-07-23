from base.views import BaseView
from balances import serializers
from service.requests.balances.get_balance import GetBalance
from service.requests.balances.get_locks import GetLocks
from service.requests.balances.transfer import Transfer


class GetBalances(BaseView):

    serializer_class = serializers.GetBalancesSerializer
    action_class = GetBalance


class Locks(BaseView):

    serializer_class = serializers.GetLocksSerializer
    action_class = GetLocks


class Transfers(BaseView):

    serializer_class = serializers.TransferSerializer
    action_class = Transfer