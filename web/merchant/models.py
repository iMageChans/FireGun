from django.db import models


class MerchantExpiry(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    expiry_date = models.CharField(max_length=255, default="1567958400")

    def __str__(self):
        return f"{self.account_id}"