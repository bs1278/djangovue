from rest_framework import viewsets
from posts import models
from posts import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    