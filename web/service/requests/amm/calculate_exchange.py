from service.contracts.base_class import Currency
from service.requests.base import abs_class
from service.utils.token_rate_calculation import TokenRateCalculation


class CalculateExchange(abs_class.Fire):
    def __init__(self, validated_data):
        super().__init__(validated_data)
        token_rate_calculation = TokenRateCalculation()
        from_currency = Currency(validated_data['from_currency'])
        to_currency = Currency(validated_data['to_currency'])
        try:
            self.res = token_rate_calculation.get_currency_rate_amount(from_currency.value, to_currency.value, validated_data['from_amount'])
            self.success = True
        except ValueError as e:
            self.res = e
            self.success = False

    def results(self):
        return self.res

    def is_success(self):
        return self.success
