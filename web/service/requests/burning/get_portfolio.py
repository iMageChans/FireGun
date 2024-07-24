from django.core.exceptions import ObjectDoesNotExist

from service.requests.base import abs_class
from users_profile.serializers import *
from service.tools.celery_update_or_create import *


class GetPortfolio(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        try:
            self.user_burning_profile = UserBurningProfile.objects.get(pk=self.account_id.mate_data_address())
        except ObjectDoesNotExist:
            self.user_burning_profile = update_or_create_burning_profile(self.account_id.mate_data_address())

    def results(self):
        if self.user_burning_profile is None:
            return None
        return UserBurningProfileSerializer(self.user_burning_profile).data

    def is_success(self):
        return self.user_burning_profile is not None