from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser


class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView): # TODO use RetrieveUpdateDestroy?
    queryset = Post.objects.all() # not using postobjects on purpose!
    serializer_class = PostSerializer
