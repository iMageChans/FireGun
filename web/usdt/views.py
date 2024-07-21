from base.views import BaseView
from usdt import serializers
from service.requests.usdt.approve import Approve
from service.requests.usdt.decrease_allowance import DecreaseAllowance
from service.requests.usdt.increase_allowance import IncreaseAllowance
from service.requests.usdt.transfer import Transfer
from service.requests.usdt.transfer_from import TransferFrom
from service.requests.usdt.balance_of import BalanceOf
from service.requests.usdt.total_supply import TotalSupply


class ApproveView(BaseView):

    serializer_class = serializers.ApproveSerializer
    action_class = Approve


class DecreaseAllowanceView(BaseView):

    serializer_class = serializers.DecreaseAllowanceSerializer
    action_class = DecreaseAllowance


class IncreaseAllowanceView(BaseView):

    serializer_class = serializers.IncreaseAllowanceSerializer
    action_class = IncreaseAllowance


class TransferView(BaseView):

    serializer_class = serializers.TransferSerializer
    action_class = Transfer


class TransferFromView(BaseView):

    serializer_class = serializers.TransferFromSerializer
    action_class = TransferFrom


class BalanceOfView(BaseView):

    serializer_class = serializers.BalanceOfSerializer
    action_class = BalanceOf


class TotalSupplyView(BaseView):
    serializer_class = serializers.TotalSupplySerializer
    action_class = TotalSupply