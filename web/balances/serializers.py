from rest_framework import serializers
from balances.models import D9Balance


class D9BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = D9Balance
        fields = '__all__'


class GetBalancesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)


class GetLocksSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)


class TransferSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)