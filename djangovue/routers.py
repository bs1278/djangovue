from rest_framework import routers
from posts import apis

router = routers.DefaultRouter()

router.register(r'posts', apis.PostViewSet)