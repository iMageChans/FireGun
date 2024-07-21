from rest_framework import serializers


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