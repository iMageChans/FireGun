from service.pallets import voting
from service.requests.base import abs_class


class ChangeCandidateSupportShare(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        percent = validated_data['percent']
        extrinsics = voting.VotingExtrinsics()
        call = extrinsics.change_candidate_support_share(percent)
        nonce = extrinsics.chain_interface.query('System', 'Account', [self.keypair.ss58_address])
        extrinsic = extrinsics.chain_interface.create_signed_extrinsic(call=call, keypair=self.keypair, nonce=nonce.value_serialized['nonce'])
        self.res = extrinsics.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)

    def results(self):
        return self.res.extrinsic.value_serialized

    def is_success(self):
        return self.res.is_success