from django.urls import path

from master_service import views

urlpatterns = [
    path('', views.backend_info, name='backend_info'),
    path('receive_routine', views.receive_routine, name='receive_routine'),
]
