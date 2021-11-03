from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

# # these were for the old individual views
# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), # show one post
#     path('', PostList.as_view(), name='listcreate'), # show all posts
# ] 