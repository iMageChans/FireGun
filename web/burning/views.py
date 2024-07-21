from base.views import BaseView
from burning import serializers
from service.requests.burning.burning import Token
from service.requests.burning.withdraw import Withdraw
from service.requests.burning.get_ancestors import GetAncestors
from service.requests.burning.get_total_burned import GetTotalBurned
from service.requests.burning.get_portfolio import GetPortfolio


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