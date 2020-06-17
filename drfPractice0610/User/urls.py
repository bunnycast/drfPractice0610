from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from User.views import UserViewSet

router = SimpleRouter()
router.register(r'api/users', UserViewSet, basename='users')

urlpatterns = [
    url(r'api-token-auth/', views.obtain_auth_token),
]

urlpatterns += router.urls

