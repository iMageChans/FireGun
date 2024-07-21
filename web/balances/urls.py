from django.urls import path
from .views import GetBalances, Locks, Transfers

urlpatterns = [
    path('get-balances/', GetBalances.as_view(), name='get-balances'),
    path('get-locks/', Locks.as_view(), name='get-locks'),
    path('transfers/', Transfers.as_view(), name='transfers'),
]