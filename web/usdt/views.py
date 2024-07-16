from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import keypair
from service.contracts import usdt
from utils.accounts import get_valid_address


class ApproveView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).approve(spender=request.data['spender'], amount=request.data['amount'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class DecreaseAllowanceView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).decrease_allowance(spender=request.data['spender'], delta_value=request.data['delta_value'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class IncreaseAllowanceView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).increase_allowance(spender=request.data['spender'], delta_value=request.data['delta_value'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class TransferView(APIView):

    def post(self, request):
        to = get_valid_address(request.data['to'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).transfer(to=to, value=request.data['value'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class TransferFromView(APIView):

    def post(self, request):
        from_ = get_valid_address(request.data['from'])
        to = get_valid_address(request.data['to'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).transfer_from(from_=from_, to=to, value=request.data['value'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class BalanceOfView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).balance_of(owner=request.data['owner'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class TotalSupplyView(APIView):
    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = usdt.USDT(key).total_supply()
        data = {'data': res.value['result']['Ok']['data']['Ok']}
        return Response(status=status.HTTP_200_OK, data=data)