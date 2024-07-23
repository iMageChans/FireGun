from burning.models import BurningTotal
from service.contracts import main_mining
from celery import shared_task

from users_profile.models import UserBurningProfile
from service.tools.celery_update_or_create import *
from service.utils.accounts import *


@shared_task
def get_burning_totals():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = main_mining.MainMining(keypair).get_total_burned()
    res = extractor.get_data_or_err(extrinsic.value_serialized)
    first_burning_totals = BurningTotal.objects.all().first()

    if first_burning_totals:
        first_burning_totals.totals = res
        first_burning_totals.save()
        return {"status": "updated", "totals": first_burning_totals.totals}
    else:
        first_burning_totals = BurningTotal.objects.create(totals=res)
        return {"status": "created", "totals": first_burning_totals.totals}


@shared_task
def update_or_create_user_burning_profile_celery(data):
    user_burning_profile, created = UserBurningProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": user_burning_profile.account_id, "created": created})
