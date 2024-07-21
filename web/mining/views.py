from base.views import BaseView
from mining import serializers
from service.requests.mining_pool.get_accumulative_reward_pool import GetAccumulativeRewardPool
from service.requests.mining_pool.get_merchant_volment import GetMerchantVolment
from service.requests.mining_pool.get_session_volume import GetSessionVolume
from service.requests.mining_pool.get_total_volume import GetTotalVolume


class AccumulativeRewardPoolView(BaseView):
    serializer_class = serializers.GetAccumulativeRewardPoolSerializer
    action_class = GetAccumulativeRewardPool


class MerchantVolmentView(BaseView):
    serializer_class = serializers.GetMerchantVolmentSerializer
    action_class = GetMerchantVolment


class SessionVolumeView(BaseView):
    serializer_class = serializers.GetSessionVolumeSerializer
    action_class = GetSessionVolume


class TotalVolumeView(BaseView):
    serializer_class = serializers.GetTotalVolumeSerializer
    action_class = GetTotalVolume
