from django.urls import path
from .views import (ReservesView,
                    LiquidityProviderView,
                    AddLiquidityView,
                    RemoveLiquidityView,
                    CheckNewLiquidityView,
                    GetD9View,
                    GetUSDTView,
                    CalculateExchangeView,
                    EstimateExchangeView,
                    CheckUSDTBalanceView)

urlpatterns = [
    path('reserves/', ReservesView.as_view(), name='amm-reserves'),
    path('liquidity-provider/', LiquidityProviderView.as_view(), name='amm-liquidity-provider'),
    path('add-liquidity/', AddLiquidityView.as_view(), name='amm-add-liquidity'),
    path('remove-liquidity/', RemoveLiquidityView.as_view(), name='amm-remove-liquidity'),
    path('check-new-liquidity/', CheckNewLiquidityView.as_view(), name='amm-check-new-liquidity'),
    path('get-d9/', GetD9View.as_view(), name='amm-get-d9'),
    path('get-usdt/', GetUSDTView.as_view(), name='amm-get-usdt'),
    path('calculate-exchange/', CalculateExchangeView.as_view(), name='amm-calculate-exchange'),
    path('estimate-exchange/', EstimateExchangeView.as_view(), name='amm-estimate-exchange'),
    path('check-usdt-balance/', CheckUSDTBalanceView.as_view(), name='amm-check-usdt-balance'),
]