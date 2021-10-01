from django.contrib import admin
from django.urls import include, path

from movies.urls import movies_router

from .views import ping

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ping/", ping, name="ping"),
    path("api/", include(movies_router.urls)),
]
