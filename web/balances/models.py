from django.db import models


class D9Balance(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    balance_d9 = models.CharField(max_length=255, default="0", blank=True, null=True)

    def __str__(self):
        return f"{self.account_id}"
