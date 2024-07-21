from service.contracts import mining_pool
from service.utils import types
from service.requests.base import abs_class


class GetAccumulativeRewardPool(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = mining_pool.MiningPool(self.keypair)
        self.res = self.call.get_accumulative_reward_pool()

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True