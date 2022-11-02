from django.urls import path, include

from .views import *

urlpatterns = [
    path("product_create/", Product_Create_ViewSet.as_view({'post': 'create'})),

]
