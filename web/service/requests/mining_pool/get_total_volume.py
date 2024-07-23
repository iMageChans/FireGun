from service.contracts import mining_pool
from service.utils import types
from service.requests.base import abs_class
from service.utils.json import extractor


class GetTotalVolume(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = mining_pool.MiningPool(self.keypair)
        self.res = self.call.get_total_volume()

    def results(self):
        return {
            "provider": extractor.get_data_or_err(self.res.value_serialized)
        }

    def is_success(self):
        extractor.get_data_or_err(self.res.value_serialized)
        if extractor.check:
            return True
        return False