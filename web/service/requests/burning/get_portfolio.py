from service.requests.base import abs_class
from users_profile.serializers import UserBurningProfileSerializer


class GetPortfolio(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.update_or_create_burning_profile_read()

    def results(self):
        if self.user_burning_profile is None:
            return None
        return UserBurningProfileSerializer(self.user_burning_profile).data

    def is_success(self):
        return self.user_burning_profile is not None