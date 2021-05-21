from django.urls import path
from rest_framework import routers

from . import views

app_name = 'rateable'

router = routers.DefaultRouter()
router.register('', views.RateableViewSet)

urlpatterns = router.urls

urlpatterns += [

]

