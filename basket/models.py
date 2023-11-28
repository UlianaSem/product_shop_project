from django.conf import settings
from django.db import models

from shop.models import Product


class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь",
                                related_name="basket")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзины"


class ProductInBasket(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name="корзина", related_name='products')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт")
    number = models.PositiveIntegerField(verbose_name="количество в корзине", default=1)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "продукт в корзине"
        verbose_name_plural = "продукты в корзине"
