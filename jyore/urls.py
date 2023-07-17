from django.urls import path
from .views import index,login_page,register,logout_view,marketplace,housesellerprofile,profile_view,delete_v,verify_otp, viewproperty,sellfirst,landsellerprofile,landviewproperty,delete_land
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name = 'home'),
    path('login/',login_page,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout_view,name='logout'),
    path('marketplace/',marketplace,name='marketplace'),
    path('housesellerprofile/',housesellerprofile,name='housesellerprofile'),
    path('profile/', profile_view, name='profile'),
    path("delete/<int:id>/",delete_v,name="delete_v"),
    path('verify-otp/<str:username>', verify_otp, name='verify_otp'),
    path('viewproperty/<int:id>/', viewproperty, name='viewproperty'),
    path('sellfirst/',sellfirst,name='sellfirst'),
    path('landsellerprofile/',landsellerprofile,name='landsellerprofile'),
    path('landviewproperty/<int:id>/', landviewproperty, name='landviewproperty'),
    path("delete_land/<int:id>/",delete_land,name="delete_land"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)