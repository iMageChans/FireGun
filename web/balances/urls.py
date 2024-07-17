from django.urls import path
from .views import GetBalances, GetLocks, Transfer

urlpatterns = [
    path('get-balances/', GetBalances.as_view(), name='get-balances'),
    path('get-locks/', GetLocks.as_view(), name='get-locks'),
    path('transfer/', Transfer.as_view(), name='transfer'),
]