from django.urls import path
from .views import AccumulativeRewardPoolView, MerchantVolmentView, SessionVolumeView, TotalVolumeView

urlpatterns = [
    path('get-accumulative-reward-pool/', AccumulativeRewardPoolView.as_view(), name='get-accumulative-reward-pool'),
    path('get-merchant-volment/', MerchantVolmentView.as_view(), name='get-merchant-volment'),
    path('get-session-volume/', SessionVolumeView.as_view(), name='get-session-volume'),
    path('get-total-volume/', TotalVolumeView.as_view(), name='get-total-volume'),

]