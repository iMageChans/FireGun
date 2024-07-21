from rest_framework import serializers


class GetNumberOfCandidatesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class CurrentSessionIndexSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)


class ValidatorStatsSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    validator_id = serializers.CharField(required=True)


class GetNodeAccumulativeVotesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class GetNodeMetadataSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)


class NodeToUserVoteTotalsSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    node_id = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)


class GetSessionNodeListSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    session_index = serializers.IntegerField(required=True)


class AddVotingInterestSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    beneficiary_voter = serializers.CharField(required=True)
    amount_to_burn = serializers.IntegerField(required=True)


class ChangeCandidateNameSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class ChangeCandidateSupportShareSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    percent = serializers.IntegerField(required=True)


class DelegateVotesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    delegations = serializers.ListField(required=True)


class RedistributeVotesSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)
    from_candidate = serializers.CharField(required=True)
    to_candidate = serializers.IntegerField(required=True)


class RemoveCandidacySerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)