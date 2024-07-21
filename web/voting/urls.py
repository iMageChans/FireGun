from django.urls import path
from .views import (GetNumberOfCandidatesView,
                    GetNumberOfCandidatesView,
                    ValidatorStatsView,
                    GetNodeAccumulativeVotesView,
                    GetNodeMetadataView,
                    NodeToUserVoteTotalsView,
                    GetSessionNodeListView,
                    AddVotingInterestView,
                    ChangeCandidateNameView,
                    ChangeCandidateSupportShareView,
                    DelegateVotesView,
                    RedistributeVotesView,
                    RemoveCandidacyView)

urlpatterns = [
    path('get-number-of-candidates/', GetNumberOfCandidatesView.as_view(), name='get-number-of-candidates'),
    path('current-session-index/', GetNumberOfCandidatesView.as_view(), name='current-session-index'),
    path('validator-stats/', ValidatorStatsView.as_view(), name='validator-stats'),
    path('get-node-accumulative-votes/', GetNodeAccumulativeVotesView.as_view(), name='get-node-accumulative-votes'),
    path('get-node-metadata/', GetNodeMetadataView.as_view(), name='get-node-metadata'),
    path('node-to-user-vote-totals/', NodeToUserVoteTotalsView.as_view(), name='node-to-user-vote-totals'),
    path('get-session-node-list/', GetSessionNodeListView.as_view(), name='get-session-node-list'),
    path('add-voting-interest/', AddVotingInterestView.as_view(), name='add-voting-interest'),
    path('change-candidate-name/', ChangeCandidateNameView.as_view(), name='change-candidate-name'),
    path('change-candidate-support-share/', ChangeCandidateSupportShareView.as_view(), name='change-candidate-support-share'),
    path('delegate-votes/', DelegateVotesView.as_view(), name='delegate-votes'),
    path('redistribute-votes/', RedistributeVotesView.as_view(), name='redistribute-votes'),
    path('remove-candidacy/', RemoveCandidacyView.as_view(), name='remove-candidacy'),
]