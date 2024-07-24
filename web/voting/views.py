from base.views import BaseView
from voting import serializers
from service.requests.voting.get_number_of_candidates import GetNumberOfCandidates
from service.requests.voting.current_session_index import CurrentSessionIndex
from service.requests.voting.validator_stats import ValidatorStats
from service.requests.voting.get_node_accumulative_votes import GetNodeAccumulativeVotes
from service.requests.voting.get_node_metadata import GetNodeMetadata
from service.requests.voting.node_to_user_vote_totals import NodeToUserVoteTotals
from service.requests.voting.get_session_node_list import GetSessionNodeList
from service.requests.voting.add_voting_interest import AddVotingInterest
from service.requests.voting.change_candidate_name import ChangeCandidateName
from service.requests.voting.change_candidate_support_share import ChangeCandidateSupportShare
from service.requests.voting.delegate_votes import DelegateVotes
from service.requests.voting.redistribute_votes import RedistributeVotes
from service.requests.voting.remove_candidacy import RemoveCandidacy
from rest_framework import viewsets
from .models import Ranks
from .serializers import RanksSerializer


class GetNumberOfCandidatesView(BaseView):

    serializer_class = serializers.GetNumberOfCandidatesSerializer
    action_class = GetNumberOfCandidates


class CurrentSessionIndexView(BaseView):

    serializer_class = serializers.GetNumberOfCandidatesSerializer
    action_class = CurrentSessionIndex


class ValidatorStatsView(BaseView):

    serializer_class = serializers.ValidatorStatsSerializer
    action_class = ValidatorStats


class GetNodeAccumulativeVotesView(BaseView):

    serializer_class = serializers.GetNodeAccumulativeVotesSerializer
    action_class = GetNodeAccumulativeVotes


class GetNodeMetadataView(BaseView):

    serializer_class = serializers.GetNodeMetadataSerializer
    action_class = GetNodeMetadata


class NodeToUserVoteTotalsView(BaseView):

    serializer_class = serializers.NodeToUserVoteTotalsSerializer
    action_class = NodeToUserVoteTotals


class GetSessionNodeListView(BaseView):

    serializer_class = serializers.GetSessionNodeListSerializer
    action_class = GetSessionNodeList


class AddVotingInterestView(BaseView):

    serializer_class = serializers.AddVotingInterestSerializer
    action_class = AddVotingInterest


class ChangeCandidateNameView(BaseView):

    serializer_class = serializers.ChangeCandidateNameSerializer
    action_class = ChangeCandidateName


class ChangeCandidateSupportShareView(BaseView):

    serializer_class = serializers.ChangeCandidateSupportShareSerializer
    action_class = ChangeCandidateSupportShare


class DelegateVotesView(BaseView):

    serializer_class = serializers.DelegateVotesSerializer
    action_class = DelegateVotes


class RedistributeVotesView(BaseView):

    serializer_class = serializers.RedistributeVotesSerializer
    action_class = RedistributeVotes


class RemoveCandidacyView(BaseView):

    serializer_class = serializers.RemoveCandidacySerializer
    action_class = RemoveCandidacy


class RanksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ranks.objects.all().order_by('-accumulative_votes')
    serializer_class = RanksSerializer