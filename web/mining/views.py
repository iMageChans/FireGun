from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.contracts import mining_pool


class AccumulativeRewardPoolView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = mining_pool.MiningPool(key).get_accumulative_reward_pool()
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class MerchantVolmentView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = mining_pool.MiningPool(key).get_merchant_volment()
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class SessionVolumeView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = mining_pool.MiningPool(key).get_session_volume(request.data['session_index'])
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)


class TotalVolumeView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = mining_pool.MiningPool(key).get_total_volume()
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)
