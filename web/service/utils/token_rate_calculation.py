from decimal import Decimal

from amm.models import CurrencyReserves
from service.utils import numbers


class TokenRateCalculation:
    def __init__(self):
        pass

    def rate(self, balance_0, balance_1, amount_0):
        try:
            # 将输入值转换为 Decimal 类型以确保高精度计算
            fixed_balance_0 = Decimal(balance_0)
            fixed_balance_1 = Decimal(balance_1)
            fixed_amount_0 = Decimal(amount_0)

            # 计算恒定乘积 k
            fixed_curve_k = fixed_balance_0 * fixed_balance_1

            # 计算新的 balance_0
            new_balance_0 = fixed_balance_0 + fixed_amount_0

            # 计算新的 balance_1，如果除以零则抛出异常
            new_balance_1 = fixed_curve_k / new_balance_0

            # 计算减少的 amount_1
            amount_1 = fixed_balance_1 - new_balance_1

            # 返回结果，转换回 float 类型
            return float(amount_1)
        except Exception as err:
            raise ValueError("Division by zero occurred", err)

    def get_currency_rate_amount(self, from_currency, to_currency, amount):
        first_currency_reserve = CurrencyReserves.objects.all().first()
        usdt = numbers.format_number(int(first_currency_reserve.usdt), 2)
        d9 = numbers.format_number(int(first_currency_reserve.d9))
        if from_currency == "USDT" and to_currency == "D9":
            res = self.rate(usdt, d9, amount)
        elif from_currency == "D9" and to_currency == "USDT":
            res = self.rate(d9, usdt, amount)
        else:
            raise ValueError("Currency must be either USDT or D9")
        return res



