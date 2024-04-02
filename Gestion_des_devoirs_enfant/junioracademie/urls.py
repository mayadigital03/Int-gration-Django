from django.urls import path
from . import views
urlpatterns = [

    path('about/', about, name='about'),
]
