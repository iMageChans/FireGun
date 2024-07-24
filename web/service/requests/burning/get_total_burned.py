from service.utils import numbers
from service.requests.base import abs_class
from burning.models import BurningTotal


class GetTotalBurned(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.burning_total = BurningTotal.objects.all().first()

    def results(self):
        return numbers.DecimalTruncator(4).format_d9(self.burning_total.totals)

    def is_success(self):
        if self.burning_total is not None:
            return True
        return False