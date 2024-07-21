from rest_framework import serializers


class SubscribeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    usdt_base_units = serializers.IntegerField(required=True)


class RedeemSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    usdt_base_units = serializers.IntegerField(required=True)


class GivePointsD9Serializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    consumer_id = serializers.CharField(required=True)
    d9_amount = serializers.IntegerField(required=True)


class GivePointsUSDTSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    consumer_id = serializers.CharField(required=True)
    usdt_amount = serializers.IntegerField(required=True)


class USDTPaymentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    merchant_id = serializers.CharField(required=True)
    usdt_amount = serializers.IntegerField(required=True)


class D9PaymentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    merchant_id = serializers.CharField(required=True)
    d9_amount = serializers.IntegerField(required=True)


class GetMerchantExpirySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)


class GetAccountSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)