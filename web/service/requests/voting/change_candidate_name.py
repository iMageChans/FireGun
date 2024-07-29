from service.pallets import voting
from service.requests.base import abs_class


class ChangeCandidateName(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        name = validated_data['name']
        extrinsics = voting.VotingExtrinsics()
        call = extrinsics.change_candidate_name(name)
        nonce = extrinsics.chain_interface.get_account_nonce(self.keypair.ss58_address)
        try:
            extrinsic = extrinsics.chain_interface.create_signed_extrinsic(call=call, keypair=self.keypair, nonce=nonce)
            self.res = extrinsics.chain_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        except Exception as e:
            print("error:", e)

    def results(self):
        return self.res.error_message

    def is_success(self):
        return self.res.is_success