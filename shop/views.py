from rest_framework.generics import ListAPIView

from shop.models import Category, Product
from shop.paginators import CategoryPaginator, ProductPaginator
from shop.serializers import ProductSerializer, CategorySerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPaginator


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator
