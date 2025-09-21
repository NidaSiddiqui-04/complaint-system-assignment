from. import views
from django.urls import path


app_name='complaint'
urlpatterns=[
    path('add/',views.add_complaint,name='add_complaint'),
    path('my_complaint/',views.my_complaints,name='my_complaint'),
    path('all_complaints/',views.all_complaints,name='all_complaints'),
    path('<int:id>/',views.update_status,name='update_status'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
]