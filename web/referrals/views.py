from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.pallets import referrals
from service.utils.accounts import get_valid_address


class GetReferral(APIView):

    def post(self, request):
        if 'account_id' not in request.data:
            try:
                key = keypair.get_keypair(request.data['keypair'])
                valid_address = key.ss58_address
            except ValueError:
                return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        else:
            valid_address = get_valid_address(request.data['account_id'])
        print(valid_address)
        res = referrals.ReferralsQueries().direct_referrals_count(valid_address)

        data = {
            "referrals": res,
            "metadata": {
                "referrals": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)
