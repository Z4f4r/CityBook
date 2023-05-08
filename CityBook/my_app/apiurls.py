from django.urls import path
from .views import EstablishmentsAPIList, EstablishmentsAPIInfo


urlpatterns = [
    path('establishmentslist/', EstablishmentsAPIList.as_view()),
    path('establishmentsinfo/', EstablishmentsAPIInfo.as_view())
]
