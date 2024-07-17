from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.contracts import node_reward


class VoteLimitView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).get_vote_limit()
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class WithdrawRewardView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).withdraw_reward(key.ss58_address)
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class SessionRewardsDataView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).get_session_rewards_data(request.data['session_index'])
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class NodeRewardsDataView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).get_node_rewards_data(key.ss58_address)
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class SetAuthorizedReceiverView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).set_authorized_receiver(node_id=request.data['node_id'], receiver_id=request.data['receiver_id'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class RemoveAuthorizedReceiverView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = node_reward.NodeReward(key).remove_authorized_receiver(node_id=request.data['node_id'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})