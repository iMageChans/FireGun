from django.db import models


class UserBurningProfile(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    amount_burned = models.CharField(max_length=255)
    balance_due = models.CharField(max_length=255)
    balance_paid = models.CharField(max_length=255)
    last_withdrawal = models.CharField(max_length=255)
    last_burn = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.account_id}"


class UserProfile(models.Model):
    account_id = models.CharField(max_length=255, primary_key=True)
    account_name = models.CharField(max_length=255, default="default", blank=True, null=True)
    balance_d9 = models.CharField(max_length=255, default="0", blank=True, null=True)
    balance_usdt = models.CharField(max_length=255, default="0", blank=True, null=True)
    node_name = models.CharField(max_length=255, default="0", blank=True, null=True)
    node_reward = models.CharField(max_length=255, default="0", blank=True, null=True)
    d9_equal_usdt = models.CharField(max_length=255, default="0", blank=True, null=True)
    usdt_equal_usdt = models.CharField(max_length=255, default="0", blank=True, null=True)
    total_value = models.CharField(max_length=255, default="0", blank=True, null=True)

    def __str__(self):
        return f"{self.account_id}"
