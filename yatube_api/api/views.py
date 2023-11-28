import logging
from rest_framework import viewsets
from posts.models import Post
from .serializers import PostSerializer

# Настройка логгера
logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # Логируем информацию о текущем пользователе
        user = self.request.user
       

        serializer.save(author=user)