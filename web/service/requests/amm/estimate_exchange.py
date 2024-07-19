from service.contracts.base_class import Direction, Currency
from service.utils import keystone, types
from service.contracts import market_maker
from service.utils.numbers import format_number


class EstimateExchange:
    def __init__(self, validated_data):
        try:
            keypair = keystone.check_keypair(validated_data['keypair'])
            direction = Direction(Currency(validated_data['from_currency']).value,
                                  Currency(validated_data['to_currency']).value)
            from_amount = validated_data['from_amount']
        except ValueError as err:
            raise err

        res = market_maker.MarketMaker(keypair).get_reserves()
        values = types.validate_res(res.value)

        keys = ['d9', 'usdt']
        data = dict(zip(keys, values))
        self.d9 = format_number(data['d9'])
        self.usdt = format_number(data['usdt'], 2)

        if Currency.USDT is Currency(validated_data['from_currency']) and Currency.D9 is Currency(
                validated_data['to_currency']):
            self.result = {
                "totals": "{:.3f}".format(self.usdt / self.d9 * from_amount)[:-1]
            }
        else:
            self.result = {
                "totals": "{:.3f}".format(self.d9 / self.usdt * from_amount)[:-1]
            }

    def results(self):
        return self.result