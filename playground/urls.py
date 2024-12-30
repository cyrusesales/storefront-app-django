from django.urls import path
from . import views

# URLConf module, means url configuration
urlpatterns = [
    path('hello/', views.say_hello)
]