from substrateinterface import Keypair
from node.models import VoteLimit
from service.contracts import node_reward
from service.utils.env import config
from service.utils.json import extractor
from celery import shared_task


@shared_task
def get_vote_limit_celery():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = node_reward.NodeReward(keypair).get_vote_limit()
    res = extractor.get_data_or_err(extrinsic.value_serialized)
    vote_limit = VoteLimit.objects.all().first()

    if vote_limit:
        vote_limit.totals = res
        vote_limit.save()
        return {"status": "updated", "totals": vote_limit.totals}
    else:
        vote_limit = VoteLimit.objects.create(totals=res)
        return {"status": "created", "totals": vote_limit.totals}