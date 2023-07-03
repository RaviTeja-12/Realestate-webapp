from django.urls import path
from . import views
urlpatterns = [
    path('inbox', views.messages_page,name='inbox'),
    path('create_thread/<str:property_username>/', views.create_thread, name='create_thread'),
]
