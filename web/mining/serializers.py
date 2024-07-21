from rest_framework import serializers


class GetAccumulativeRewardPoolSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetMerchantVolmentSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class GetSessionVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    session_index = serializers.IntegerField(required=True)


class GetTotalVolumeSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)