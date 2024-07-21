from service.contracts import node_reward
from service.utils import types
from service.requests.base import abs_class
from service.utils.accounts import get_valid_address


class SetAuthorizedReceiver(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = node_reward.NodeReward(self.keypair)
        node_id = get_valid_address(validated_data['node_id'])
        receiver = get_valid_address(validated_data['receiver'])
        self.res = self.call.set_authorized_receiver(node_id, receiver)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True