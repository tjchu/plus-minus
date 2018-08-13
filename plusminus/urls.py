from django.urls import path

from plusminus import views

app_name = 'plusminus'
urlpatterns = [
    path('', views.index),
    path('results/', views.results),
]
