from base.views import BaseView
from node import serializers
from service.requests.node.get_vote_limit import GetVoteLimit
from service.requests.node.withdraw_reward import WithdrawReward
from service.requests.node.get_session_rewards_data import GetSessionRewardsData
from service.requests.node.get_node_rewards_data import GetNodeRewardsData
from service.requests.node.set_authorized_receiver import SetAuthorizedReceiver
from service.requests.node.remove_authorized_receiver import RemoveAuthorizedReceiver


class VoteLimitView(BaseView):
    serializer_class = serializers.GetVoteLimitSerializer
    action_class = GetVoteLimit


class WithdrawRewardView(BaseView):
    serializer_class = serializers.WithdrawRewardSerializer
    action_class = WithdrawReward


class SessionRewardsDataView(BaseView):
    serializer_class = serializers.GetSessionRewardsDataSerializer
    action_class = GetSessionRewardsData


class NodeRewardsDataView(BaseView):
    serializer_class = serializers.GetNodeRewardsDataSerializer
    action_class = GetNodeRewardsData


class SetAuthorizedReceiverView(BaseView):
    serializer_class = serializers.SetAuthorizedReceiverSerializer
    action_class = SetAuthorizedReceiver


class RemoveAuthorizedReceiverView(BaseView):
    serializer_class = serializers.RemoveAuthorizedReceiverSerializer
    action_class = RemoveAuthorizedReceiver