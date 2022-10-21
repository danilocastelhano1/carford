from rest_framework import routers
from django.urls import include, path
from api.views import PersonViewset


router = routers.DefaultRouter()
router.register(r"person", PersonViewset)


urlpatterns = [
    path(r"", include(router.urls)),
]
