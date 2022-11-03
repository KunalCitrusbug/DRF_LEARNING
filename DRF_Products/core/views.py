from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Product, Brand
from core.paginations import CustomPagination
from core.serializers import ProductSerializer, ProductListSerializer, BrandSerializer
from rest_framework.authtoken.models import Token


# =================Create User Token====================
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.pk,
            'username': user.username,
            'token': token.key
        })


# =================Product List====================
class Generic_Product_list(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# ==============Create Product====================
class Product_Create_ViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', ]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

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
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# ============Update Product========================
class Product_Update(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# ============Delete Product========================
class Product_Delete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductSerializer
    lookup_field = 'id'


# ============Search Product or Brand========================
class Search(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'brand__brand']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
