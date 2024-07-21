from rest_framework import serializers


class DirectReferralsCountSerializer(serializers.Serializer):
    keypair = serializers.CharField(required=True)