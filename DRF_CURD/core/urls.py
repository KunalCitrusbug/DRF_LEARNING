from .views import *
from django.urls import path

urlpatterns = [
    path('profile/', profile),
    path('class_profile/', Class_Profile.as_view()),
    path('generic_profile/get/', Generic_Profile_GET.as_view()),
    path('generic_profile/post/', Generic_Profile_POST.as_view()),
    path('generic_profile/del/<int:id>/', Generic_Profile_DELETE.as_view()),
    path('generic_profile/update/<int:id>/', Generic_Profile_UPDATE.as_view()),
]
