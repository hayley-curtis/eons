from django.urls import  path 
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name = "asterisms"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:region>/', views.regions, name= 'regions'),
    path('<str:region>/<str:culture>/', views.culture_detail, name = 'culture_detail'),
    path('<str:region>/<str:culture>/<asterism>/', views.asterism_detail, name = 'asterism_detail'),
    path('about', views.about, name = 'about')
]

urlpatterns += staticfiles_urlpatterns()
