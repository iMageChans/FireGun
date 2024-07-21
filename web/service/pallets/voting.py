from service.utils.types import Delegation
from typing import List
from service.pallets.base_class import PalletQueriesBase, PalletExtrinsicsBase, config


class VotingQueries(PalletQueriesBase):
    def __init__(self):
        super().__init__('D9NodeVoting')

    def get_number_of_candidates(self):
        """
        gets number of candidates
        Returns:
            int: number of candidates
        """
        result = self.compose_query('CurrentNumberOfCandidatesNodes', [])
        return result.value

    def current_session_index(self):
        """
        gets current session index
        Returns:
            int: current session index
        """
        result = self.compose_query('CurrentSessionIndex', [])
        return result.value

    def validator_stats(self, validator_id: str):
        """
        gets validator stats
        Returns:
            dict: validator stats
        """
        result = self.compose_query('CurrentValidatorVoteStats', [validator_id])
        return result.value

    def get_node_accumulative_votes(self, node_id: str):
        """
        gets node accumulative votes
        Returns:
            dict: node accumulative votes
        """
        result = self.compose_query('NodeAccumulativeVotes', [node_id])
        return result.value

    def get_node_metadata(self, node_id: str):
        """
        gets node metadata
        Returns:
            dict: node metadata
        """
        result = self.compose_query('NodeMetadata', [node_id])
        return result.value

    def node_to_user_vote_totals(self, node_id: str, user_id: str | None = None):
        """
        gets node to user vote totals
        Returns:
            list: (supporter_id, votes)
        """
        result = self.chain_interface.query_map('D9NodeVoting', 'NodeToUserVotesTotals')
        node_supporters = []
        if user_id == None:
            for node_user_tuple, votes in result:
                if node_user_tuple[0].value == node_id:
                    node_supporters.append((node_user_tuple[1].value, votes.value))
            return node_supporters
        else:
            result = self.compose_query('NodeToUserVotesTotals', [node_id, user_id])

    def get_session_node_list(self, session_index: int):
        """
        gets session node list
        Returns:
            list: nodes
        """
        result = self.compose_query('SessionNodeList', [session_index])
        return result.value


class VotingExtrinsics(PalletExtrinsicsBase):

    def __init__(self):
        super().__init__('D9NodeVoting')

    def add_voting_interest(self, beneficiary_voter: str, amount_to_burn: int):
        """
        adds voting interest
        Args:
            beneficiary_voter: beneficiary voter
            amount_to_burn: amount to burn in base units
        Returns:
        GenericCall
          """
        func_params = {
            'beneficiaryVoter': beneficiary_voter,
            'mainPool': config.get('MAIN_POOL_CONTRACT'),
            'amountToBurn': amount_to_burn,
            'burnContract': config.get('BURN_CONTRACT')
        }
        self.compose_call('AddVotingInterest', func_params)

    def change_candidate_name(self, name: str):
        """
        changes candidate name
        Args:
            name (str): name in hexadecimal format
        Returns:
            GenericCalls
            """
        self.compose_call("ChangeCandidateName", {'name': name})

    def change_candidate_support_share(self, percent: int):
        """
        changes candidate support share
        Args:
            percent (int): percent
        Returns:
            GenericCall
          """
        if percent > 100 or percent < 0:
            raise ValueError("percent must be between 0 and 100")
        self.compose_call("ChangeCandidateSupportShare", {'percent': percent})

    def delegate_votes(self, delegations: List[Delegation]):
        """
        delegates votes
        Args:
            delegations (List[Delegation]): delegations
        Returns:
            GenericCall
          """
        self.compose_call("DelegateVotes", {'delegations': delegations})

    def redistribute_votes(self, from_candidate: str, to_candidate: str):
        """
        redistribute votes
        Args:
            from_candidate (str): from candidate
            to_candidate (str): to candidate
        Returns:
            GenericCall
           """
        self.compose_call("RedistributeVotes", {'from': from_candidate, 'to': to_candidate})

    def remove_candidacy(self):
        """
        removes candidacy
        Args:
            candidate_id (str): candidate id
        Returns:
            GenericCall
          """
        self.compose_call("RemoveCandidacy")