from django.urls import path
from .views import BurningTotalView, BurningAncestorsView, BurningWithdrawView, BurningView, BurningPortfolioView

urlpatterns = [
    path('token/', BurningView.as_view(), name='burning-token'),
    path('withdraw/', BurningWithdrawView.as_view(), name='burning-withdraw'),
    path('ancestors/', BurningAncestorsView.as_view(), name='burning-ancestors'),
    path('totals/', BurningTotalView.as_view(), name='burning-total'),
    path('portfolio/', BurningPortfolioView.as_view(), name='burning-portfolio'),
]