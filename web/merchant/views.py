from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils import keypair
from service.contracts import merchant
from utils.accounts import get_valid_address


class SubscribeView(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['account_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).subscribe(valid_address, request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class RedeemView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).redeem_d9()
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GivePointsD9View(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['consumer_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).give_points_d9(valid_address, request.data['d9'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GivePointsUSDTView(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['consumer_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).give_points_usdt(valid_address, request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class USDTPaymentView(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['merchant_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).send_usdt_payment_to_merchant(valid_address, request.data['usdt'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class D9PaymentView(APIView):

    def post(self, request):
        valid_address = get_valid_address(request.data['merchant_id'])
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).send_d9_payment_to_merchant(valid_address, request.data['d9'])
        if res.is_success:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GetMerchantExpiryView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).get_merchant_expiry(key.ss58_address)
        print(res.value)
        # if res.is_success:
        return Response(status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})


class GetAccountView(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = merchant.Merchant(key).get_account(key.ss58_address)
        print(res.value)
        # if res.is_success:
        return Response(status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': 'Transaction failed'})