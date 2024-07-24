from celery import shared_task

from service.tools.celery_update_or_create import *
from service.utils.env import config
from service.utils.json import extractor
from users_profile.models import UserProfile
from service.contracts.usdt import USDT
from service.pallets.balances import BalancesQueries
from service.utils import accounts


@shared_task
def update_or_create_user_burning_profile_celery(account_id):
    update_or_create_burning_profile(account_id=account_id)
    print({"account_id": account_id})

@shared_task
def update_or_create_merchant_expiry_celery(account_id):
    update_or_create_merchant_expiry(account_id=account_id)
    print({"account_id": account_id})


@shared_task
def update_or_create_usdt_balance_celery(account_id):
    update_or_create_d9_balance(account_id=account_id)
    print({"account_id": account_id})


@shared_task
def update_or_create_d9_balance_celery(account_id):
    update_or_create_d9_balance(account_id=account_id)
    print({"account_id": account_id})


@shared_task
def update_or_create_user_profile(data):
    user_profile_data = {}
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)

    account_id = accounts.ValidAddress(data['account_id'])
    get_balance = BalancesQueries().get_balance(account_id.get_valid_address())
    balances_d9 = extractor.get_balances_d9(get_balance)

    usdt_balance = USDT(keypair).balance_of(account_id.get_valid_address())

    user_profile_data['account_id'] = account_id
    user_profile_data['balances_d9'] = balances_d9
    user_profile_data['balance_usdt'] = usdt_balance

    user_profile, created = UserProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=user_profile_data
    )
    print({"account_id": user_profile.account_id, "created": created})