from base.views import BaseView
from referrals import serializers
from service.requests.referrals.direct_referrals_count import DirectReferralsCount


class GetReferral(BaseView):

    serializer_class = serializers.DirectReferralsCountSerializer
    action_class = DirectReferralsCount
