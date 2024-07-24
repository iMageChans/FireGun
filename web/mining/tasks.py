from substrateinterface import Keypair
from mining.models import AccumulativeRewardPool, MerchantVolume, TotalVolume
from service.contracts import mining_pool
from service.utils.env import config
from service.utils.json import extractor
from celery import shared_task


@shared_task
def get_accumulative_reward_pool_celery():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = mining_pool.MiningPool(keypair).get_accumulative_reward_pool()
    res = extractor.get_data_or_err(extrinsic.value_serialized)
    accumulative_reward_pool = AccumulativeRewardPool.objects.all().first()

    if accumulative_reward_pool:
        accumulative_reward_pool.totals = res
        accumulative_reward_pool.save()
        return {"status": "updated", "totals": accumulative_reward_pool.totals}
    else:
        accumulative_reward_pool = AccumulativeRewardPool.objects.create(totals=res)
        return {"status": "created", "totals": accumulative_reward_pool.totals}


@shared_task
def get_merchant_volume_celery():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = mining_pool.MiningPool(keypair).get_merchant_volume()
    res = extractor.get_data_or_err(extrinsic.value_serialized)
    merchant_volume = MerchantVolume.objects.all().first()

    if merchant_volume:
        merchant_volume.totals = res
        merchant_volume.save()
        return {"status": "updated", "totals": merchant_volume.totals}
    else:
        merchant_volume = MerchantVolume.objects.create(totals=res)
        return {"status": "created", "totals": merchant_volume.totals}


@shared_task
def get_total_volume_celery():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = mining_pool.MiningPool(keypair).get_total_volume()
    res = extractor.get_data_or_err(extrinsic.value_serialized)
    total_volum = TotalVolume.objects.all().first()

    if total_volum:
        total_volum.totals = res
        total_volum.save()
        return {"status": "updated", "totals": total_volum.totals}
    else:
        total_volum = TotalVolume.objects.create(totals=res)
        return {"status": "created", "totals": total_volum.totals}