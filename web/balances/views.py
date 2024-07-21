from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from balances import serializers
from service.requests.balances.get_balance import GetBalance
from service.requests.balances.get_locks import GetLocks
from service.requests.balances.transfer import Transfer


class GetBalances(APIView):

    def post(self, request):
        serializer = serializers.GetBalancesSerializer(data=request.data)
        if serializer.is_valid():
            res = GetBalance(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class Locks(APIView):

    def post(self, request):
        serializer = serializers.GetBalancesSerializer(data=request.data)
        if serializer.is_valid():
            res = GetLocks(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class Transfers(APIView):

    def post(self, request):
        serializer = serializers.TransferSerializer(data=request.data)
        if serializer.is_valid():
            res = Transfer(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)