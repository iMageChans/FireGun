from django.urls import path
from .views import (ApproveView,
                    DecreaseAllowanceView,
                    IncreaseAllowanceView,
                    TransferView,
                    TransferFromView,
                    BalanceOfView,
                    TotalSupplyView)

urlpatterns = [
    path('approve/', ApproveView.as_view(), name='approve'),
    path('decrease-allowance/', DecreaseAllowanceView.as_view(), name='decrease-allowance'),
    path('increase-allowance/', IncreaseAllowanceView.as_view(), name='increase-allowance'),
    path('transfer/', TransferView.as_view(), name='transfer'),
    path('transfer-from/', TransferFromView.as_view(), name='transfer-from'),
    path('balances/', BalanceOfView.as_view(), name='balance-of'),
    path('total-supply/', TotalSupplyView.as_view(), name='total-supply')
]