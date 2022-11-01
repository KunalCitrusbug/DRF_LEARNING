from django.urls import path, include

from .views import *

urlpatterns = [
    path("product_create/", Product_Create_ViewSet.as_view({'post': 'create'})),
    path("brand_create/", Generic_Brand_Create.as_view()),
    path("product_list/", Generic_Product_list.as_view()),
    path("product_update/<int:id>/", Product_Update.as_view()),
    path("product_delete/<int:id>/", Product_Delete.as_view()),
    path("search/", Search.as_view()),

]
