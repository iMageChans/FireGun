from substrateinterface import Keypair
from amm.models import CurrencyReserves
from service.contracts import market_maker
from service.utils.env import config
from service.utils.json import extractor
from service.utils import numbers
from celery import shared_task


@shared_task
def get_currency_reserves():
    private_key = config.get_private_key()
    keypair = Keypair.create_from_private_key(private_key, ss58_format=9)
    extrinsic = market_maker.MarketMaker(keypair).get_reserves()
    res = extractor.d9_to_usdt(extrinsic.value_serialized)
    first_currency_reserve = CurrencyReserves.objects.all().first()

    if first_currency_reserve:
        first_currency_reserve.d9 = res['d9']
        first_currency_reserve.usdt = res['usdt']
        first_currency_reserve.d9_to_usdt = float(numbers.DecimalTruncator(4).format_usdt(res['usdt'])) / float(numbers.DecimalTruncator(4).format_d9(res['d9']))
        first_currency_reserve.usdt_to_d9 = float(numbers.DecimalTruncator(4).format_d9(res['d9'])) / float(numbers.DecimalTruncator(4).format_usdt(res['usdt']))
        first_currency_reserve.save()
        return {"status": "updated", "d9": first_currency_reserve.d9, "usdt": first_currency_reserve.usdt, "d9_to_usdt": first_currency_reserve.d9_to_usdt, "usdt_to_d9": first_currency_reserve.usdt_to_d9}
    else:
        first_currency_reserve = CurrencyReserves.objects.create(d9=res['d9'], usdt=res['usdt'])
        return {"status": "created", "d9": first_currency_reserve.d9, "usdt": first_currency_reserve.usdt}