from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Product, Brand
from core.paginations import CustomPagination
from core.serializers import ProductSerializer, ProductListSerializer, BrandSerializer


# =================Product List====================
class Generic_Product_list(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination


# ==============Create Product====================
class Product_Create_ViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', ]

    def create(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        data = {
            "name": self.request.POST.get('name'),
            "price": self.request.POST.get('price'),
            "brand": Brand.objects.get(brand=self.request.POST.get('brand')).id
        }
        _serializer = self.serializer_class(data=data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(data=_serializer.data)
        else:
            return Response(data=_serializer.errors)


# ==================Create Brand====================
class Generic_Brand_Create(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = BrandSerializer


# ============Update Product========================
# class Product_Update(viewsets.ViewSet):
#     queryset = Product.objects.all()
#
#     serializer_class = ProductSerializer
#
#     def update(self, request, *args, **kwargs):
#         data = self.request.data
#         obj = Product.objects.get(id=kwargs.get("id"))
#         serializer = ProductSerializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data)
#         else:
#             return Response(serializer.errors)

class Product_Update(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
# ============Delete Product========================
class Product_Delete(generics.DestroyAPIView):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    lookup_field = 'id'


# ============Search Product or Brand========================
class Search(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'brand__brand']
