from django.urls import path

from . import views

urlpatterns = [
    #path('', views.main_view)
    path('', views.MainView.as_view(), name='main')
]