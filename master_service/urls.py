from django.urls import path
from master_service import views

urlpatterns = [
    path('', views.backend_info, name='backend_info'),
    path('receiveRoutine', views.receive_routine, name='receive_routine'),
]
