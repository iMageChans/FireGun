from rest_framework import serializers


class ApproveSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    spender = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)


class DecreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    spender = serializers.CharField(required=True)
    delta_value = serializers.IntegerField(required=True)


class IncreaseAllowanceSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    spender = serializers.CharField(required=True)
    delta_value = serializers.IntegerField(required=True)


class TransferSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)


class TransferFromSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    from_address = serializers.CharField(required=True)
    to_address = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)


class BalanceOfSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    owner = serializers.CharField(required=True)


class TotalSupplySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)