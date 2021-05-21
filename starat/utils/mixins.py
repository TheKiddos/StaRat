from rest_framework.permissions import AllowAny


class PublicListRetrieveViewSetMixin:
    """Allow anyone to use list and retrieve actions, return default permissions and auth otherwise"""
    allowed_actions = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.allowed_actions:
            return [AllowAny(), ]
        return super().get_permissions()
