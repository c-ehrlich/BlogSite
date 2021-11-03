from rest_framework import generics, viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    DjangoModelPermissionsOrAnonReadOnly,
)


class PostUserWritePermission(BasePermission):
    """Posts can only be edited or deleted by their author"""

    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:  # GET, OPTIONS, HEAD
            return True

        return obj.author == request.user  # is the person trying to edit the author?


class PostList(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Post.postobjects.all()

    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


# viewsets.ViewSet methods
#     def list(self, request)
#     def create(self, request)
#     def retrieve(self, request, pk=None)
#     def update(self, request, pk=None)
#     def partial_update(self, request, pk=None)
#     def destroy(self, request, pk=None)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()  # not using postobjects on purpose!
#     serializer_class = PostSerializer
