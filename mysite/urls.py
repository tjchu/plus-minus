"""mysite URL Configuration."""

from django.contrib import admin
from django.urls import include, path

from plusminus import views as plusminus_views

urlpatterns = [
    path('', plusminus_views.index, name='home'),
    path('polls/', include('polls.urls')),
    path('plusminus/', include('plusminus.urls')),
    path('admin/', admin.site.urls),
]

