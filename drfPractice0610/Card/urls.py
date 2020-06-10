from rest_framework.routers import SimpleRouter
from Card.views import CardViewSet

router = SimpleRouter()
router.register(r'api/cards', CardViewSet, basename='cards')

urlpatterns = router.urls
