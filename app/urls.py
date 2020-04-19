from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.conf.urls import include

from .views.login_view import LoginView
from .views.logout_view import LogoutView
from .views.user_view import UserView
from .views.neighborhood_view import NeighborhoodView
from .views.city_view import CityView
from .views.state_view import StateView
from .views.address_view import AddressView

from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"user", UserView)
router.register(r"neighborhood", NeighborhoodView)
router.register(r"city", CityView)
router.register(r"state", StateView)
router.register(r"address", AddressView)

router.register(r'device/apns', APNSDeviceAuthorizedViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)

app_name = "app"

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^login/", LoginView.as_view()),
    url(r"^logout/", LogoutView.as_view()),
]
