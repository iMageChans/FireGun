from django.db import models


class CurrencyReserves(models.Model):
    d9 = models.CharField(max_length=255, default="0")
    usdt = models.CharField(max_length=255, default="0")
    d9_to_usdt = models.CharField(max_length=255, default="0")
    usdt_to_d9 = models.CharField(max_length=255, default="0")

    def __str__(self):
        return f"{self.d9} - {self.usdt}"


class ExchangeRate(models.Model):
    d9 = models.CharField(max_length=255, default="0")
    usdt = models.CharField(max_length=255, default="0")

    def __str__(self):
        return f"{self.d9} - {self.usdt}"