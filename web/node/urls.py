from django.urls import path
from .views import VoteLimitView, WithdrawRewardView, SessionRewardsDataView, NodeRewardsDataView, SetAuthorizedReceiverView, RemoveAuthorizedReceiverView

urlpatterns = [
    path('get-vote-limit/', VoteLimitView.as_view(), name='get-vote-limit'),
    path('withdraw-reward/', WithdrawRewardView.as_view(), name='withdraw-reward'),
    path('get-session-rewards-data/', SessionRewardsDataView.as_view(), name='get-session-rewards-data'),
    path('get-node-rewards-data/', NodeRewardsDataView.as_view(), name='get-node-rewards-data'),
    path('set-authorized-receiver/', SetAuthorizedReceiverView.as_view(), name='set-authorized-receiver'),
    path('remove-authorized-receiver/', RemoveAuthorizedReceiverView.as_view(), name='remove-authorized-receiver'),
]