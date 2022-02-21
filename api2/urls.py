# Routers provide an easy way of automatically determining the URL conf.
from django.urls import path, include
from rest_framework import routers

from api2.views import UserViewSet

router = routers.DefaultRouter() # api2 로 이동
router.register(r'users', UserViewSet) # api2 로 이동

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)), # api2 로 이동
]