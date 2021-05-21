from rest_framework import serializers
from .models import Rateable


class RateableSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, rateable):
        return self.context["request"].build_absolute_uri(rateable.get_absolute_url())

    class Meta:
        model = Rateable
        fields = (
            'id',
            'name',
            'type',
            'url'
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Set the owner of the object as the authenticated user"""

        user = self.context["request"].user
        if not user.is_authenticated:
            raise ValueError("Attempting to create a Rateable object without an owner")
        validated_data["owner"] = user
        return super(RateableSerializer, self).create(validated_data)
