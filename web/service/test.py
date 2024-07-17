from substrateinterface import Keypair
from pallets import balances
from substrateinterface.exceptions import SubstrateRequestException

from service.utils.interface import D9Interface
from service.utils.env import config
from service.utils.numbers import to_number


d9_interface = D9Interface(
    url=config.get('MAIN_NET_URL'),  # 这里使用了 Polkadot 主网的 RPC 端点
    ss58_format=9,                # ss58 格式，0 代表 Polkadot 主网
    type_registry_preset='polkadot'
)

balances = balances.BalancesExtrinsics()




# 生成的助记词: gas marble jealous tree any dilemma total jeans divide huge minimum fiber
# keypair <Keypair (address=5EUxvwDN8shTuadTBH2pmVaG1WAHVmyM2GZakcmER32kPHbL)>
# 地址: 5EUxvwDN8shTuadTBH2pmVaG1WAHVmyM2GZakcmER32kPHbL
# 公钥: b'j\xf9\x19G\xef\xdb\x12\xa21V$\x87>\x98\xc6\x8a\xd5|\xc9\xf4\xf7\x84\xfb\x18\x19\xd0\xd4\xaf\x1a>ez'
# 测试地址：znS9gMrWUKvGAkJwWx7DybEJpgqHGPPUv1ix2QtnYXZLZu2

# mnemonic = Keypair.generate_mnemonic()
send_address = "znS9gMrWUKvGAkJwWx7DybEJpgqHGPPUv1ix2QtnYXZLZu2"
mnemonic = 'blast curve early try fold fall plastic hobby donkey tomato crater diet'
private_key = '57601f83cf6a8bf585aad5cbcae7442dc73e5fa6b130a425c4bf4b8a0dc4080e8c592adb084f1da8fcc443677e6c8a1b5e2ada0e3859005cbe5b689c8f5151b7'
print("生成的助记词:", mnemonic)

keypair = Keypair.create_from_mnemonic(mnemonic, ss58_format=9)
private_key_keypair = Keypair.create_from_private_key(private_key, ss58_format=9)


nonce = d9_interface.query('System', 'Account', [private_key_keypair.ss58_address]).value['nonce']
call = balances.transfer(send_address, to_number(10))
extrinsic = d9_interface.create_signed_extrinsic(call=call, keypair=keypair, nonce=nonce)
try:
    receipt = d9_interface.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_hash}'")
    if receipt.is_success:
        print("Transaction successful")
    else:
        print("Transaction failed")
except SubstrateRequestException as e:
    print(f"Failed to send: {e}")


print("keypair:", keypair.ss58_address)
print("private_key_keypair:", private_key_keypair.ss58_address)
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

# voting_queries = VotingQueries()
# number = voting_queries.get_number_of_candidates()
# address_list = voting_queries.get_session_node_list(number)
#
# for address in address_list:
#     node = voting_queries.get_node_metadata(address)
#     vote = voting_queries.get_node_accumulative_votes(address)