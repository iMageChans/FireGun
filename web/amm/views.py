from base.views import BaseView
from amm import serializers
from service.requests.amm.get_reserves import GetReserves
from service.requests.amm.get_liquidity_provider import GetLiquidityProvider
from service.requests.amm.add_liquidity import AddLiquidity
from service.requests.amm.remove_liquidity import RemoveLiquidity
from service.requests.amm.check_new_liquidity import CheckNewLiquidity
from service.requests.amm.get_d9 import GetD9
from service.requests.amm.get_usdt import GetUSDT
from service.requests.amm.calculate_exchange import CalculateExchange
from service.requests.amm.estimate_exchange import EstimateExchange
from service.requests.amm.check_usdt_balance import CheckUSDTBalance


class ReservesView(BaseView):

    serializer_class = serializers.GetReservesSerializer
    action_class = GetReserves


class LiquidityProviderView(BaseView):

    serializer_class = serializers.GetLiquidityProviderSerializer
    action_class = GetLiquidityProvider


class AddLiquidityView(BaseView):

    serializer_class = serializers.AddLiquiditySerializer
    action_class = AddLiquidity


class RemoveLiquidityView(BaseView):

    serializer_class = serializers.RemoveLiquiditySerializer
    action_class = RemoveLiquidity


class CheckNewLiquidityView(BaseView):

    serializer_class = serializers.CheckNewLiquiditySerializer
    action_class = CheckNewLiquidity


class GetD9View(BaseView):

    serializer_class = serializers.GetD9Serializer
    action_class = GetD9


class GetUSDTView(BaseView):

    serializer_class = serializers.GetUSDTSerializer
    action_class = GetUSDT


class CalculateExchangeView(BaseView):

    serializer_class = serializers.CalculateExchangeSerializer
    action_class = CalculateExchange


class EstimateExchangeView(BaseView):

    serializer_class = serializers.EstimateExchangeSerializer
    action_class = EstimateExchange


class CheckUSDTBalanceView(BaseView):

    serializer_class = serializers.CheckUSDTBalanceSerializer
    action_class = CheckUSDTBalance