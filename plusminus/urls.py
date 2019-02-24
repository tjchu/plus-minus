from django.conf.urls import url

from plusminus import views

app_name = 'plusminus'
urlpatterns = [
    url('', views.index),
    url('results/', views.results),
]
