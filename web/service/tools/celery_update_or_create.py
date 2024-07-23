from substrateinterface import Keypair

from balances.models import D9Balance
from service.utils.env import config
from usdt.models import USDTBalance
from service.contracts import usdt
from service.pallets import balances
from service.utils import numbers
from service.utils.accounts import ValidAddress
from service.utils.json import extractor


def update_or_create_d9_balance(account_id):

    valid_address = ValidAddress(account_id)

    data = {
        "account_id": valid_address.mate_data_address()
    }

    call = balances.BalancesQueries()
    res = call.get_balance(account_id=valid_address.get_valid_address())
    data.update({"balance_d9": numbers.DecimalTruncator(4).format_d9(extractor.get_balances_d9(res))})
    data.update({"account_id": valid_address.mate_data_address()})

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
    data.update({"account_id": valid_address.mate_data_address()})

    usdt_balance, created = USDTBalance.objects.update_or_create(
        account_id=data['account_id'],
        defaults=data
    )
    print({"account_id": usdt_balance.account_id, "balance_usdt": usdt_balance.balance_usdt, "created": created})
    return usdt_balance
