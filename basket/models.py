from django.conf import settings
from django.db import models

from shop.models import Product


class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт")
    number = models.PositiveIntegerField(verbose_name="количество в корзине")

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "продукт в корзине"
        verbose_name_plural = "продукты в корзине"


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", null=True, blank=True)

    products = models.ManyToManyField(ProductInBasket, verbose_name="товары")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзины"
