from rest_framework import status

from base.views import BaseView
from burning import serializers
from burning.models import BurningTotal
from rest_framework.response import Response
from service.requests.burning.burning import Token
from service.requests.burning.withdraw import Withdraw
from service.requests.burning.get_ancestors import GetAncestors
from service.requests.burning.get_total_burned import GetTotalBurned
from service.requests.burning.get_portfolio import GetPortfolio
from service.utils.numbers import get_return_percent, DecimalTruncator


class BurningView(BaseView):
    serializer_class = serializers.BurningSerializer
    action_class = Token


class BurningWithdrawView(BaseView):
    serializer_class = serializers.BurningWithdrawSerializer
    action_class = Withdraw


class BurningAncestorsView(BaseView):
    serializer_class = serializers.GetAncestorsSerializer
    action_class = GetAncestors


class BurningTotalView(BaseView):
    serializer_class = serializers.GetTotalBurnedSerializer
    action_class = GetTotalBurned


class BurningPortfolioView(BaseView):
    serializer_class = serializers.GetPortfolioSerializer
    action_class = GetPortfolio


class BurningGlobalComputingPowerView(BaseView):

    def post(self, request):
        burning_total = BurningTotal.objects.all().first()
        if burning_total is not None:
            totals = DecimalTruncator(3).format_d9(float(burning_total.totals))
            data = get_return_percent(float(totals))
            return Response(status=status.HTTP_200_OK, data={'results': data})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


