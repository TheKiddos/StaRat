from rest_framework import viewsets, authentication, permissions, mixins
from .models import Rateable, Rating
from . import serializers
from utils.mixins import PublicListRetrieveViewSetMixin


# TODO: Make Public And Private View Instead?
class RateableViewSet(PublicListRetrieveViewSetMixin,
                      viewsets.ModelViewSet):
    """Manage Ratable Objects By Owners"""

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Rateable.objects.all()
    serializer_class = serializers.RateableSerializer
    filterset_fields = ['type', 'name']

    def get_queryset(self):
        """
        Restrict Operations to authenticated users rateable objects if the user is authenticated

        This is used so owner of rateable objects don't modify except their objects while other guest user can see everything
        """

        qs = super(RateableViewSet, self).get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs


class RatingViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """A viewset that provides `create`, and `list` actions."""

    permission_classes = (permissions.AllowAny,)
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    filterset_fields = ['rateable', 'reviewer', 'stars']
