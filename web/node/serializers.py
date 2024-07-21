from rest_framework import serializers


class GetVoteLimitSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class WithdrawRewardSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class GetSessionRewardsDataSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    session_index = serializers.IntegerField(required=True)


class GetNodeRewardsDataSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class SetAuthorizedReceiverSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)
    receiver = serializers.CharField(required=True)


class RemoveAuthorizedReceiverSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)