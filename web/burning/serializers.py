from rest_framework import serializers


class BurningSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)

    # def validate_amount(self, value):
    #     if value < 100:
    #         raise serializers.ValidationError("Amount must be at least 100.")
    #     return value

