from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.nodelist, name='node-list'),
    path('<str:pk>/',views.nodedetail, name='node-detail')
]