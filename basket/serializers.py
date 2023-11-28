from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from rest_framework.validators import UniqueTogetherValidator

from basket.models import Basket, ProductInBasket
from shop.models import Product


class BasketRetrieveSerializer(ModelSerializer):
    number = SerializerMethodField()
    amount = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ["products", 'number', "amount", ]

    def get_number(self, instance):
        return sum([product.number for product in instance.products.all()])

    def get_amount(self, instance):
        amount = 0

        for product in instance.products.all():
            price = Product.objects.get(pk=product.product.pk).price
            amount += product.number * price

        return amount


class BasketSerializer(ModelSerializer):

    class Meta:
        model = Basket
        fields = "__all__"


class ProductInBasketSerializer(ModelSerializer):

    class Meta:
        model = ProductInBasket
        fields = "__all__"
        validators = [UniqueTogetherValidator(queryset=ProductInBasket.objects.all(), fields=['basket', 'product'])]


class UpdateProductInBasketSerializer(ModelSerializer):
    basket = PrimaryKeyRelatedField(read_only=True)
    product = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProductInBasket
        fields = "__all__"
