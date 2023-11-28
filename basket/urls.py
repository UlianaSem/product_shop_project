from django.urls import path
from rest_framework.routers import DefaultRouter

from basket.apps import BasketConfig
from basket.views import BasketRetrieveAPIView, BasketDestroyAPIView, ProductInBasketAPIViewSet

app_name = BasketConfig.name

router = DefaultRouter()
router.register('', ProductInBasketAPIViewSet, basename='manage_product')

urlpatterns = [
    path('total/<int:pk>/', BasketRetrieveAPIView.as_view(), name="total"),
    path('clear/<int:pk>/', BasketDestroyAPIView.as_view(), name="clear"),
] + router.urls
