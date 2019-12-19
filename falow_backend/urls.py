from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.ViewSets.ProfileViewSet import ProfileViewSet
from api.ViewSets.PostViewSet import PostViewSet
from api.ViewSets.LikeViewSet import LikeViewSet
from api.ViewSets.CommentViewSet import CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/profile', ProfileViewSet)
router.register(r'api/post', PostViewSet)
router.register(r'api/like', LikeViewSet)
router.register(r'api/comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login')
]
