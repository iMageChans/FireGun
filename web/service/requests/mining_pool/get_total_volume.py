from service.requests.base import abs_class
from mining.models import TotalVolume


class GetTotalVolume(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.total_volume = TotalVolume.objects.all().first()

    def results(self):
        return self.total_volume.totals

    def is_success(self):
        if self.total_volume is not None:
            return True
        return False