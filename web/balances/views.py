from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.pallets.balances import BalancesQueries, BalancesExtrinsics
from service.utils.accounts import get_valid_address
from service.utils.numbers import format_number, to_number
from substrateinterface.exceptions import SubstrateRequestException


class GetBalances(APIView):

    def post(self, request):
        if 'account_id' not in request.data:
            try:
                key = keypair.get_keypair(request.data['keypair'])
                valid_address = key.ss58_address
            except ValueError:
                return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        else:
            valid_address = get_valid_address(request.data['account_id'])
        res = BalancesQueries().get_balance(valid_address)

        data = {
            "balance": format_number(res),
            "metadata": {
                "balance": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class GetLocks(APIView):

    def post(self, request):
        if 'account_id' in request.data:
            valid_address = get_valid_address(request.data['account_id'])
        else:
            try:
                key = keypair.get_keypair(request.data['keypair'])
                valid_address = key.ss58_address
            except ValueError:
                return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        res = BalancesQueries().get_locks(valid_address)

        data = {
            "locks": res,
            "metadata": {
                "locks": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class Transfer(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        valid_address = get_valid_address(request.data['to'])
        balances = BalancesExtrinsics()
        transfer = balances.transfer(valid_address, to_number(request.data['amount']))
        nonce = balances.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = balances.chain_interface.create_signed_extrinsic(call=transfer, keypair=key, nonce=nonce)
        try:
            res = balances.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})