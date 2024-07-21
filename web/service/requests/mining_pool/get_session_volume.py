from service.contracts import mining_pool
from service.utils import types
from service.requests.base import abs_class


class GetSessionVolume(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        session_index = validated_data['session_index']
        self.call = mining_pool.MiningPool(self.keypair)
        self.res = self.call.get_session_volume(session_index)

    def results(self):
        return types.validate_res(self.call.gas_predit_result.value_serialized)

    def is_success(self):
        if "Err" in types.validate_res(self.call.gas_predit_result.value_serialized):
            return False
        return True