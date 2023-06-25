from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogViewPage.as_view(), name='home')
]