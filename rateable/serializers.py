from rest_framework import serializers
from .models import Rateable, Rating


class RateableSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_url(self, rateable):
        return self.context["request"].build_absolute_uri(rateable.get_absolute_url())

    def get_average_rating(self, rateable):
        return rateable.get_average_rating()

    class Meta:
        model = Rateable
        fields = (
            'id',
            'name',
            'type',
            'url',
            'average_rating',
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Set the owner of the object as the authenticated user"""

        user = self.context["request"].user
        if not user.is_authenticated:
            raise ValueError("Attempting to create a Rateable object without an owner")
        validated_data["owner"] = user
        return super(RateableSerializer, self).create(validated_data)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'rateable',
            'reviewer',
            'stars',
            'review'
        )
        read_only_fields = ('id',)
