from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from amm import serializers
from service.requests.amm.get_reserves import GetReserves
from service.requests.amm.get_liquidity_provider import GetLiquidityProvider
from service.requests.amm.add_liquidity import AddLiquidity
from service.requests.amm.remove_liquidity import RemoveLiquidity
from service.requests.amm.check_new_liquidity import CheckNewLiquidity
from service.requests.amm.get_d9 import GetD9
from service.requests.amm.get_usdt import GetUSDT
from service.requests.amm.calculate_exchange import CalculateExchange
from service.requests.amm.estimate_exchange import EstimateExchange
from service.requests.amm.check_usdt_balance import CheckUSDTBalance


class ReservesView(APIView):

    def post(self, request):
        serializer = serializers.GetReservesSerializer(data=request.data)
        if serializer.is_valid():
            res = GetReserves(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LiquidityProviderView(APIView):

    def post(self, request):
        serializer = serializers.GetLiquidityProviderSerializer(data=request.data)
        if serializer.is_valid():
            res = GetLiquidityProvider(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class AddLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.AddLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            res = AddLiquidity(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class RemoveLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.RemoveLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            res = RemoveLiquidity(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CheckNewLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.CheckNewLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            res = CheckNewLiquidity(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class GetD9View(APIView):

    def post(self, request):
        serializer = serializers.GetD9Serializer(data=request.data)
        if serializer.is_valid():
            res = GetD9(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class GetUSDTView(APIView):

    def post(self, request):
        serializer = serializers.GetUSDTSerializer(data=request.data)
        if serializer.is_valid():
            res = GetUSDT(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CalculateExchangeView(APIView):

    def post(self, request):
        serializer = serializers.CalculateExchangeSerializer(data=request.data)
        if serializer.is_valid():
            res = CalculateExchange(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class EstimateExchangeView(APIView):

    def post(self, request):
        serializer = serializers.EstimateExchangeSerializer(data=request.data)
        if serializer.is_valid():
            res = EstimateExchange(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CheckUSDTBalanceView(APIView):

    def post(self, request):
        serializer = serializers.CheckUSDTBalanceSerializer(data=request.data)
        if serializer.is_valid():
            res = CheckUSDTBalance(serializer.validated_data)
            data = res.results()
            if res.is_success():
                return Response(status=status.HTTP_200_OK, data={'data': data})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'data': data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)