from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView

app_name = "users"

urlpatterns = [
    # all paths are /api/user/xyz
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenView.as_view(), name="blacklist"),
]
