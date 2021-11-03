from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT token auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Main API
    path("api/", include("blog_api.urls", namespace="blog_api")),
    path("api/user/", include("users.urls", namespace="users")),
    # for web ui
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    # schema and documentation
    path("schema", get_schema_view(
        title="BlogAPI",
        description="An API for doin the blogs",
        version="0.0.1"
    ), name="openapi-schema"),
    path('docs/', include_docs_urls(title="BlogAPI")),
    # only for server debugging - maybe in the future this will show an API tutorial?
    path("", include("blog.urls", namespace="blog")),
]
