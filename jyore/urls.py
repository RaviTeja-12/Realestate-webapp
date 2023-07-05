from django.urls import path
from .views import index,login_page,register,logout_view,marketplace,sell,profile_view,delete_v
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name = 'home'),
    path('login',login_page,name='login'),
    path('register',register,name='register'),
    path('logout',logout_view,name='logout'),
    path('marketplace',marketplace,name='marketplace'),
    path('sell',sell,name='sell'),
    path('profile/', profile_view, name='profile'),
    path("delete/<int:id>/",delete_v,name="delete_v"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)