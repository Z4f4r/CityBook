from django.urls import path, include
from .views import EstablishmentsViewSet, EstablishmentsAPIList
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'establishments', EstablishmentsViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/establishmentslist/', EstablishmentsAPIList.as_view())
]
