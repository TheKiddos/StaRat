from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create', views.CreateUserView.as_view(), name='create'),
    path('token', views.CreateTokenView.as_view(), name='token'),
    path('token/refresh', views.RefreshTokenView.as_view(), name='token_refresh'),
    path('detail', views.ManageUserView.as_view(), name='detail'),
]
