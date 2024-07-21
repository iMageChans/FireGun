from base.views import BaseView
from merchant import serializers
from service.requests.merchant.subscribe import Subscribe
from service.requests.merchant.redeem_d9 import Redeem
from service.requests.merchant.give_green_points_d9 import GivePointsD9
from service.requests.merchant.give_green_points_usdt import GivePointsUSDT
from service.requests.merchant.send_d9_payment_to_merchant import D9Payment
from service.requests.merchant.send_usdt_payment_to_merchant import USDTPayment
from service.requests.merchant.get_merchant_expiry import GetMerchantExpiry
from service.requests.merchant.get_account import GetAccount


class SubscribeView(BaseView):

    serializer_class = serializers.SubscribeSerializer
    action_class = Subscribe


class RedeemView(BaseView):

    serializer_class = serializers.RedeemSerializer
    action_class = Redeem


class GivePointsD9View(BaseView):

    serializer_class = serializers.GivePointsD9Serializer
    action_class = GivePointsD9


class GivePointsUSDTView(BaseView):

    serializer_class = serializers.GivePointsUSDTSerializer
    action_class = GivePointsUSDT


class D9PaymentView(BaseView):

    serializer_class = serializers.D9PaymentSerializer
    action_class = D9Payment


class USDTPaymentView(BaseView):

    serializer_class = serializers.USDTPaymentSerializer
    action_class = USDTPayment


class GetMerchantExpiryView(BaseView):

    serializer_class = serializers.GetMerchantExpirySerializer
    action_class = GetMerchantExpiry


class GetAccountView(BaseView):

    serializer_class = serializers.GetAccountSerializer
    action_class = GetAccount