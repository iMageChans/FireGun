from rest_framework import serializers


class GetReservesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetLiquidityProviderSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)


class AddLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    usdt_amount = serializers.FloatField(required=True)
    d9_amount = serializers.FloatField(required=True)


class RemoveLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class CheckNewLiquiditySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    usdt_liquidity = serializers.IntegerField(required=True)
    d9_liquidity = serializers.IntegerField(required=True)


class GetD9Serializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    usdt = serializers.IntegerField(required=True)


class GetUSDTSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    d9_amount = serializers.IntegerField(required=True)


class CalculateExchangeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    from_currency = serializers.IntegerField(required=False)
    to_currency = serializers.IntegerField(required=False)
    from_amount = serializers.IntegerField(required=False)


class EstimateExchangeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    from_currency = serializers.IntegerField(required=False)
    to_currency = serializers.IntegerField(required=False)
    from_amount = serializers.IntegerField(required=True)


class CheckUSDTBalanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    account_id = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)