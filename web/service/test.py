
from substrateinterface import Keypair

from service.contracts.node_reward import NodeReward
from service.contracts.main_mining import MainMining
from service.contracts.mining_pool import MiningPool
from service.pallets.voting import VotingQueries


# 生成的助记词: gas marble jealous tree any dilemma total jeans divide huge minimum fiber
# keypair <Keypair (address=5EUxvwDN8shTuadTBH2pmVaG1WAHVmyM2GZakcmER32kPHbL)>
# 地址: 5EUxvwDN8shTuadTBH2pmVaG1WAHVmyM2GZakcmER32kPHbL
# 公钥: b'j\xf9\x19G\xef\xdb\x12\xa21V$\x87>\x98\xc6\x8a\xd5|\xc9\xf4\xf7\x84\xfb\x18\x19\xd0\xd4\xaf\x1a>ez'

# mnemonic = Keypair.generate_mnemonic()
mnemonic = 'blast curve early try fold fall plastic hobby donkey tomato crater diet'
private_key = '57601f83cf6a8bf585aad5cbcae7442dc73e5fa6b130a425c4bf4b8a0dc4080e8c592adb084f1da8fcc443677e6c8a1b5e2ada0e3859005cbe5b689c8f5151b7'
print("生成的助记词:", mnemonic)

keypair = Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
private_key_keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
print("地址:", keypair.ss58_address)
print("公钥:", keypair.public_key.hex())
print("私钥:", keypair.private_key.hex())

print("私钥生成地址:", keypair.ss58_address)
print("私钥生成公钥:", keypair.public_key.hex())
print("私钥生成私钥:", keypair.private_key.hex())

# node_reward = NodeReward(private_key_keypair)
# print(node_reward.get_vote_limit())
#
# main_mining = MainMining(private_key_keypair)
# print(main_mining.get_total_burned())
#
# mining_pool = MiningPool(private_key_keypair)
# print(mining_pool.get_total_volume())

voting_queries = VotingQueries()
number = voting_queries.get_number_of_candidates()
address_list = voting_queries.get_session_node_list(number)

for address in address_list:
    node = voting_queries.get_node_metadata(address)
    vote = voting_queries.get_node_accumulative_votes(address)