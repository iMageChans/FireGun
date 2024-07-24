from substrateinterface import Keypair

from balances.models import D9Balance
from usdt.models import USDTBalance
from merchant.models import MerchantExpiry
from users_profile.models import UserBurningProfile

from service.utils.env import config
from service.contracts import usdt, merchant, main_mining
from service.pallets import balances
from service.utils import numbers
from service.utils.accounts import ValidAddress
from service.utils.json import extractor


def update_or_create_merchant_profile(account_id):
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = merchant.Merchant(keypair)
    res = call.get_account(valid_address.get_valid_address())
    data.update(extractor.get_merchant_portfolio(res.value_serialized))

    user_burning_profile, created = UserBurningProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": user_burning_profile.account_id, "created": created})
    return user_burning_profile


def update_or_create_burning_profile(account_id):
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = main_mining.MainMining(keypair)
    res = call.get_portfolio(valid_address.get_valid_address())
    data.update(extractor.get_burning_portfolio(res.value_serialized))

    user_burning_profile, created = UserBurningProfile.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": user_burning_profile.account_id, "created": created})
    return user_burning_profile


def update_or_create_d9_balance(account_id):

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = balances.BalancesQueries()
    res = call.get_balance(account_id=valid_address.get_valid_address())
    data.update({"balance_d9": numbers.DecimalTruncator(4).format_d9(extractor.get_balances_d9(res))})

    d9_balance, created = D9Balance.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": d9_balance.account_id, "balance_d9": d9_balance.balance_d9, "created": created})
    return d9_balance


def update_or_create_usdt_balance(account_id):

    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = usdt.USDT(keypair)
    res = call.balance_of(owner=valid_address.get_valid_address())
    data.update({"balance_usdt": numbers.DecimalTruncator(2).format_usdt(extractor.get_data_or_err(res.value_serialized))})

    usdt_balance, created = USDTBalance.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": usdt_balance.account_id, "balance_usdt": usdt_balance.balance_usdt, "created": created})
    return usdt_balance


def update_or_create_merchant_expiry(account_id):
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = merchant.Merchant(keypair)
    res = call.get_merchant_expiry(valid_address.get_valid_address())
    data.update({"expiry_date": extractor.get_data_or_err(res.value_serialized)})

    merchant_expiry, created = MerchantExpiry.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": merchant_expiry.account_id, "expiry_date": merchant_expiry.expiry_date, "created": created})
    return merchant_expiry