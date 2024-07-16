from django.urls import path
from .views import BurningTotalView, BurningAncestorsView, BurningWithdrawView, BurningView

urlpatterns = [
    path('', BurningView.as_view(), name='burning'),
    path('withdraw/', BurningWithdrawView.as_view(), name='burning-withdraw'),
    path('ancestors/', BurningAncestorsView.as_view(), name='burning-ancestors'),
    path('total/', BurningTotalView.as_view(), name='burning-total'),

]