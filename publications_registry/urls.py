from django.urls import path

from . import views

urlpatterns = [path('overview', views.OverviewView.as_view()),
               path('overview/create_record', views.RecordCreateView.as_view()),
               path('overview/details/<int:pk>', views.RecordDisplayView.as_view()),
               path('overview/details/<int:pk>/update', views.RecordUpdateView.as_view()),
               path('overview/details/<int:pk>/delete', views.RecordDeleteView.as_view()),
               ]