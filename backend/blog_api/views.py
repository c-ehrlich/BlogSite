from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly,
)


class PostUserWritePermission(BasePermission):
    """Posts can only be edited or deleted by their author"""

    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # GET, OPTIONS, HEAD
            return True

        return obj.author == request.user  # is the person trying to edit the author?


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()  # not using postobjects on purpose!
    serializer_class = PostSerializer
