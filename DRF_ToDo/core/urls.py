from django.urls import path, include

from .views import *

urlpatterns = [
    path('task/', Task.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view())
]
