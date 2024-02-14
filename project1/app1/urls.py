from django.urls import path 
from . import views

urlpatterns = [
    path('av/',views.add_view,name='add_url'),
    path('sv/',views.show_view,name='show_url'),
    path('uv/<int:pk>/',views.update_view,name = 'update_url'),
    path('dv/<int:pk>/',views.delete_view,name = 'delete_url')
    
]