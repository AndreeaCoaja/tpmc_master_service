from rest_framework.routers import DefaultRouter

from master_service.views import ReceiveRoutineViewSet
# from master_service.views import TestMailViewSet

router = DefaultRouter()
router.register(r'receive_routine', ReceiveRoutineViewSet, basename='receive_routine')
# router.register(r'test_mail', TestMailViewSet, basename='test_mail')
urlpatterns = router.urls
