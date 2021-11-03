from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT token auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Main API
    path("api/", include("blog_api.urls", namespace="blog_api")),
    path('api/user/', include('users.urls', namespace='users')),

    # for web ui
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),

    # only for server debugging - maybe in the future this will show an API tutorial?
    path("", include("blog.urls", namespace="blog")),
]
