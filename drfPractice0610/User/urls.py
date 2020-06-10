from rest_framework.routers import SimpleRouter
from User.views import UserViewSet

router = SimpleRouter()
router.register(r'api/users', UserViewSet, basename='users')

urlpatterns = router.urls
