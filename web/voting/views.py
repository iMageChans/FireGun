from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.utils import keypair
from service.pallets import voting
from service.utils.accounts import get_valid_address
from service.utils.numbers import format_number, to_number
from substrateinterface.exceptions import SubstrateRequestException
from service.utils.types import Delegation


class GetNumberOfCandidates(APIView):

    def post(self, request):
        res = voting.VotingQueries().get_number_of_candidates()
        data = {
            "candidates_count": res,
            "metadata": {
                "candidates_count": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class CurrentSessionIndex(APIView):

    def post(self, request):
        res = voting.VotingQueries().current_session_index()
        data = {
            "session_index": res,
            "metadata": {
                "session_index": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class ValidatorStats(APIView):

    def post(self, request):
        if 'validator_id' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res = voting.VotingQueries().validator_stats(request.data['validator_id'])

        data = {
            "validator_stats": res,
            "metadata": {
                "validator_stats": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class GetNodeAccumulativeVotes(APIView):

    def post(self, request):
        if 'node_id' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res = voting.VotingQueries().get_node_accumulative_votes(request.data['node_id'])

        data = {
            "node_accumulative_votes": res,
            "metadata": {
                "node_accumulative_votes": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class GetNodeMetadata(APIView):

    def post(self, request):
        if 'node_id' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res = voting.VotingQueries().get_node_metadata(request.data['node_id'])

        data = {
            "node_metadata": res,
            "metadata": {
                "node_metadata": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class NodeToUserVoteTotals(APIView):

    def post(self, request):
        if ['node_id', 'user_id'] not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res = voting.VotingQueries().node_to_user_vote_totals(request.data['node_id'], request.data['user_id'])

        data = {
            "totals": res,
            "metadata": {
                "totals": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class GetSessionNodeList(APIView):

    def post(self, request):
        if 'session_index' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        res = voting.VotingQueries().get_session_node_list(request.data['session_index'])

        data = {
            "session_node_list": res,
            "metadata": {
                "session_node_list": res
            }
        }

        return Response(status=status.HTTP_200_OK, data=data)


class AddVotingInterest(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        valid_address = get_valid_address(request.data['beneficiary_voter'])
        votings = voting.VotingExtrinsics()
        call = votings.add_voting_interest(valid_address, request.data['amount'])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})


class ChangeCandidateName(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        votings = voting.VotingExtrinsics()
        call = votings.change_candidate_name(request.data['name'])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})


class ChangeCandidateSupportShare(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        votings = voting.VotingExtrinsics()
        call = votings.change_candidate_support_share(request.data['percent'])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})


class DelegateVotes(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        votings = voting.VotingExtrinsics()
        delegation = Delegation(request.data['candidate'], request.data['amount'])
        call = votings.delegate_votes([delegation])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})


class RedistributeVotes(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        votings = voting.VotingExtrinsics()
        call = votings.redistribute_votes(request.data['from_candidate'], request.data['to_candidate'])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})


class RemoveCandidacy(APIView):

    def post(self, request):
        try:
            key = keypair.get_keypair(request.data['keypair'])
        except ValueError:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'error': ValueError})
        votings = voting.VotingExtrinsics()
        call = votings.remove_candidacy(request.data['candidate_id'])
        nonce = votings.chain_interface.query('System', 'Account', [key.ss58_address]).value['nonce']
        extrinsic = votings.chain_interface.create_signed_extrinsic(call=call, keypair=key, nonce=nonce)
        try:
            res = votings.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
            if res.is_success:
                return Response(status=status.HTTP_200_OK)
        except SubstrateRequestException as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error': e})