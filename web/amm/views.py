from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import keypair
from service.contracts import market_maker
from utils.accounts import get_valid_address
from utils.numbers import format_number
from service.contracts.base_class import Direction


class ReservesView(APIView):

    def post(self, request):

        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).get_reserves().value
        usdt = format_number(res['result']['Ok']['data']['Ok'][1], 2)
        d9 = format_number(res['result']['Ok']['data']['Ok'][0])
        d9_to_usdt = usdt / d9
        usdt_to_d9 = d9 / usdt
        data = {
            "total": usdt * 2,
            "d9": f"{d9:.2f}",
            "usdt": f"{usdt:.2f}",
            "d9_to_usdt": f"{d9_to_usdt:.6f}",
            "usdt_to_d9": f"{usdt_to_d9:.6f}",
        }
        return Response(status=status.HTTP_200_OK, data=data)


class LiquidityProviderView(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['account_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).get_liquidity_provider(valid_address)
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class AddLiquidityView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).add_liquidity(usdt_amount=request.data['usdt'], d9_amount=request.data['d9'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class RemoveLiquidityView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).remove_liquidity()
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class CheckNewLiquidityView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).check_new_liquidity(usdt_liquidity=request.data['usdt'], d9_liquidity=request.data['d9'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GetD9View(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).get_d9(usdt=request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GetUSDTView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).get_usdt(d9_amount=request.data['d9'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class CalculateExchangeView(APIView):

    def post(self, request):
        direction = Direction(from_currency=request.data['from_currency'], to_currency=request.data['to_currency'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).calculate_exchange(direction=direction, from_amount=request.data['amount'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class EstimateExchangeView(APIView):

    def post(self, request):
        direction = Direction(from_currency=request.data['from_currency'], to_currency=request.data['to_currency'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).estimate_exchange(direction=direction, from_amount=request.data['amount'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class CheckUSDTBalanceView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = market_maker.MarketMaker(key).check_usdt_balance(account_id=request.data['account_id'], usdt_amount=request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})