# from django.urls import path
# from master_service import views
#
# urlpatterns = [
#     path('', views.backend_info, name='backend_info'),
#     path('receiveRoutine', views.receive_routine, name='receive_routine'),
# ]

from rest_framework.routers import DefaultRouter

from master_service.views import ReceiveRoutineViewSet

router = DefaultRouter()
router.register(r'', ReceiveRoutineViewSet.backend_info, basename='backend_info')
router.register(r'receiveRoutine', ReceiveRoutineViewSet.create, basename='receive_routine')
urlpatterns = router.urls
