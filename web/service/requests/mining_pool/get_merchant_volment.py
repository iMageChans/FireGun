from service.requests.base import abs_class
from mining.models import MerchantVolume


class GetMerchantVolume(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.merchant_volume = MerchantVolume.objects.all().first()

    def results(self):
        return self.merchant_volume.totals

    def is_success(self):
        if self.merchant_volume is not None:
            return True
        return False