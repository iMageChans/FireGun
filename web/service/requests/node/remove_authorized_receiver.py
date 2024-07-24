from service.contracts import node_reward
from service.utils import types
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address
from service.utils.json import extractor


class RemoveAuthorizedReceiver(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = node_reward.NodeReward(self.keypair)
        node_id = get_valid_address(validated_data['node_id'])
        self.res = self.call.remove_authorized_receiver(node_id)

    def results(self):
        if self.res.is_success:
            return extractor.get_transfer_data(self.res)
        return self.res.error_message

    def is_success(self):
        return self.res.is_success