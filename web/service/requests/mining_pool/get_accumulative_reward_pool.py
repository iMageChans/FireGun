from service.requests.base import abs_class
from mining.models import AccumulativeRewardPool


class GetAccumulativeRewardPool(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.accumulative_reward_pool = AccumulativeRewardPool.objects.all().first()

    def results(self):
        return self.accumulative_reward_pool.totals

    def is_success(self):
        if self.accumulative_reward_pool is not None:
            return True
        return False