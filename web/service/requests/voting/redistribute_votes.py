from service.pallets import voting
from service.utils.accounts import get_valid_address
from service.utils import numbers
from service.requests.base import abs_class


class RedistributeVotes(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        from_candidate = get_valid_address(validated_data['from_candidate'])
        to_candidate = get_valid_address(validated_data['to_candidate'])
        extrinsics = voting.VotingExtrinsics()
        call = extrinsics.redistribute_votes(from_candidate, to_candidate)
        nonce = extrinsics.chain_interface.query('System', 'Account', [self.keypair.ss58_address])
        extrinsic = extrinsics.chain_interface.create_signed_extrinsic(call=call, keypair=self.keypair, nonce=nonce.value_serialized['nonce'])
        self.res = extrinsics.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)

    def results(self):
        return self.res.extrinsic.value_serialized

    def is_success(self):
        return self.res.is_success