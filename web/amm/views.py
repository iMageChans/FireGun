from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keystone
from service.contracts import market_maker
from service.utils.accounts import get_valid_address
from service.utils.numbers import format_number
from service.contracts.base_class import Direction
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



class ReservesView(APIView):

    def post(self, request):
        serializer = serializers.GetReservesSerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = GetReserves(serializer.validated_data)
                return Response(status=status.HTTP_200_OK, data=res.results())
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LiquidityProviderView(APIView):

    def post(self, request):
        serializer = serializers.GetLiquidityProviderSerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = GetLiquidityProvider(serializer.validated_data)
                return Response(status=status.HTTP_200_OK, data=res.results())
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class AddLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.AddLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = AddLiquidity(serializer.validated_data)
                if res.results().is_success:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Transaction success'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Transaction failed'})
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class RemoveLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.RemoveLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = RemoveLiquidity(serializer.validated_data)
                if res.results().is_success:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Transaction success'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Transaction failed'})
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CheckNewLiquidityView(APIView):

    def post(self, request):
        serializer = serializers.CheckNewLiquiditySerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = CheckNewLiquidity(serializer.validated_data)
                if res.results().is_success:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Transaction success'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Transaction failed'})
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class GetD9View(APIView):

    def post(self, request):
        serializer = serializers.GetD9Serializer(data=request.data)
        if serializer.is_valid():
            try:
                res = GetD9(serializer.validated_data)
                if res:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Transaction success'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Transaction failed'})
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class GetUSDTView(APIView):

    def post(self, request):
        serializer = serializers.GetUSDTSerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = GetUSDT(serializer.validated_data)
                if res.results().is_success:
                    return Response(status=status.HTTP_200_OK, data={'message': 'Transaction success'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Transaction failed'})
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CalculateExchangeView(APIView):

    def post(self, request):
        serializer = serializers.CalculateExchangeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = CalculateExchange(serializer.validated_data)
                return Response(status=status.HTTP_200_OK, data=res.results())
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class EstimateExchangeView(APIView):

    def post(self, request):
        serializer = serializers.EstimateExchangeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                res = EstimateExchange(serializer.validated_data)
                return Response(status=status.HTTP_200_OK, data=res.results())
            except Exception as err:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': err})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class CheckUSDTBalanceView(APIView):

    def post(self, request):
        try:
            key = keystone.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).check_usdt_balance(account_id=request.data['account_id'], usdt_amount=request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})