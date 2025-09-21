from . import views
from django.urls import path
from django.contrib.auth import views as authviews

app_name='users'

urlpatterns=[
    path('',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]