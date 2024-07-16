from django.urls import path
from .views import (SubscribeView,
                    RedeemView,
                    GivePointsD9View,
                    GivePointsUSDTView,
                    USDTPaymentView,
                    D9PaymentView,
                    GetMerchantExpiryView,
                    GetAccountView)

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('redeem-d9/', RedeemView.as_view(), name='redeem-d9'),
    path('give-points-d9/', GivePointsD9View.as_view(), name='give-points-d9'),
    path('give-points-usdt/', GivePointsUSDTView.as_view(), name='give-points-usdt'),
    path('usdt-payment/', USDTPaymentView.as_view(), name='usdt-payment'),
    path('d9-payment/', D9PaymentView.as_view(), name='d9-payment'),
    path('get-merchant_expiry/', GetMerchantExpiryView.as_view(), name='get-merchant_expiry'),
    path('get-account/', GetAccountView.as_view(), name='get-account'),
]