from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url('', views.IndexView.as_view(), name='index'),
    url('<int:pk>/', views.DetailView.as_view(), name='detail'),
    url('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    url('<int:question_id>/vote/', views.vote, name='vote'),
]
