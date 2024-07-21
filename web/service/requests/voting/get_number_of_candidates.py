from service.pallets import voting
from service.requests.base import abs_class


class GetNumberOfCandidates(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        self.call = voting.VotingQueries()
        self.res = self.call.get_number_of_candidates()

    def results(self):
        return self.res.value_serialized

    def is_success(self):
        if "Err" in self.res.value_serialized:
            return False
        return True