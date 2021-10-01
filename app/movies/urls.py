from rest_framework import routers

from .views import MovieViewSet

movies_router = routers.DefaultRouter()
movies_router.register(r"movies", MovieViewSet)
