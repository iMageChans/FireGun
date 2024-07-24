from django.core.exceptions import ObjectDoesNotExist
from service.requests.base import abs_class
from service.tools.celery_update_or_create import *
from merchant.serializers import *


class GetMerchantExpiry(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            self.merchant_expiry = MerchantExpiry.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            self.merchant_expiry = update_or_create_merchant_expiry(self.account_id.mate_data_address())

    def results(self):
        if self.merchant_expiry is None:
            return None
        return MerchantExpirySerializer(self.merchant_expiry).data

    def is_success(self):
        return self.merchant_expiry is not None