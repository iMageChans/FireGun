from service.contracts.base_class import D9Contract
from substrateinterface import Keypair


class NodeReward(D9Contract):

    def __init__(self, keypair: Keypair):
        super().__init__('NODE_REWARD_CONTRACT', 'node_reward.json', keypair)

    def get_vote_limit(self):
        return self.contract_read('get_vote_limit')

    def withdraw_reward(self, node_id: str):
        params = {
            "node_id": node_id,
        }
        return self.contract_exec('withdraw_reward', params)

    def get_session_rewards_data(self, session_index: int):
        params = {
            "session_index": session_index,
        }
        return self.contract_read('get_session_rewards_data', params)

    def get_node_rewards_data(self, node_id: str):
        params = {
            "node_id": node_id,
        }
        return self.contract_read('get_node_reward_data', params)

    def set_authorized_receiver(self, node_id: str, receiver_id: str):
        params = {
            "node_id": node_id,
            "receiver": receiver_id,
        }
        return self.contract_exec('set_authorized_receiver', params)

    def remove_authorized_receiver(self, node_id: str):
        params = {
            "node_id": node_id,
        }
        return self.contract_exec('remove_authorized_receiver', params)