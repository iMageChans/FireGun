from service.pallets import voting
from service.utils.accounts import get_valid_address
from service.requests.base import abs_class


class NodeToUserVoteTotals(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        user_id = get_valid_address(validated_data['user_id'])
        node_id = get_valid_address(validated_data['node_id'])
        self.call = voting.VotingQueries()
        self.res = self.call.node_to_user_vote_totals(user_id, node_id)

    def results(self):
        return self.res.value_serialized['data']

    def is_success(self):
        if "Err" in self.res.value_serialized['data']:
            return False
        return True