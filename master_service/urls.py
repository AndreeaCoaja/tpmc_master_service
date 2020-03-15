from rest_framework.routers import DefaultRouter

from master_service.views import ReceiveRoutineViewSet

router = DefaultRouter()
router.register(r'receive_routine', ReceiveRoutineViewSet, basename='receive_routine')
urlpatterns = router.urls
