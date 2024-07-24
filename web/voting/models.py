from django.db import models


class Ranks(models.Model):
    node_id = models.CharField(max_length=255, primary_key=True)
    node_name = models.CharField(max_length=255)
    sharing_percent = models.CharField(max_length=255)
    accumulative_votes = models.IntegerField()

    def __str__(self):
        return f"{self.node_id}"
