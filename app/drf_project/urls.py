from django.contrib import admin
from django.urls import path, include
from movies.urls import movies_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(movies_router.urls)),
]
