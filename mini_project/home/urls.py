from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('booking',views.booking,name='booking'),
    path('doctors',views.doctors,name='doctors'),
    path('department',views.department,name='department'),
]