from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.contracts import main_mining
from burning import serializers
from service.requests.burning.burning import Token


class BurningView(APIView):

    def post(self, request):
        serializer = serializers.BurningSerializer(data=request.data)
        if serializer.is_valid():
            res = Token(serializer.validated_data)
            data = res.results()
            if res.is_success:
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class BurningWithdrawView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = main_mining.MainMining(key).withdraw()
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class BurningAncestorsView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = main_mining.MainMining(key).get_ancestors(key.ss58_address)
        print(res.value)
        # if res.is_success:
        return Response(status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class BurningTotalView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = main_mining.MainMining(key).get_total_burned()
        data = {'total': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)