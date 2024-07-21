from service.pallets import voting
from service.requests.base import abs_class


class GetSessionNodeList(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        session_index = validated_data['session_index']
        self.call = voting.VotingQueries()
        self.res = self.call.get_session_node_list(session_index)

    def results(self):
        return self.res.value_serialized['data']

    def is_success(self):
        if "Err" in self.res.value_serialized['data']:
            return False
        return True