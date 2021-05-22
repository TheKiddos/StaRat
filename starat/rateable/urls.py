from django.urls import path
from rest_framework import routers

from . import views

app_name = 'rateable'

router = routers.DefaultRouter()
router.register('rateables', views.RateableViewSet)
router.register('ratings', views.RatingViewSet)

urlpatterns = router.urls

urlpatterns += [

]

