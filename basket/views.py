from rest_framework.generics import RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from basket.models import Basket, ProductInBasket
from basket.permissions import IsOwner, IsBasketOwner
from basket.serializers import BasketRetrieveSerializer, BasketSerializer, ProductInBasketSerializer, \
    UpdateProductInBasketSerializer


class BasketRetrieveAPIView(RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketRetrieveSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BasketDestroyAPIView(DestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):
        for product in instance.products.all():
            product.delete()


class ProductInBasketAPIViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = ProductInBasket.objects.all()
    permission_classes = [IsAuthenticated, IsBasketOwner]
    default_serializer = ProductInBasketSerializer
    serializers = {
        'partial_update': UpdateProductInBasketSerializer,
        'update': UpdateProductInBasketSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
