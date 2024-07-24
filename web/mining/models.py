from django.db import models


class AccumulativeRewardPool(models.Model):
    totals = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.totals}"


class MerchantVolume(models.Model):
    totals = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.totals}"


class TotalVolume(models.Model):
    totals = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.totals}"