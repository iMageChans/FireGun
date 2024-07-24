from service.requests.base import abs_class
from node.models import VoteLimit


class GetVoteLimit(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.vote_limit = VoteLimit.objects.all().first()

    def results(self):
        return self.vote_limit.totals

    def is_success(self):
        if self.vote_limit is not None:
            return True
        return False