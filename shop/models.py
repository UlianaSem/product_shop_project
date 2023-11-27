from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(max_length=255, unique=True, verbose_name="slug-имя")
    picture = models.ImageField(upload_to='category/', verbose_name="изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")

    name = models.CharField(max_length=255, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(max_length=255, unique=True, verbose_name="slug-имя")
    picture = models.ImageField(upload_to='subcategory/', verbose_name="изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"


class Dimension(models.Model):
    height = models.PositiveIntegerField(verbose_name="высота")
    width = models.PositiveIntegerField(verbose_name="ширина")

    def __str__(self):
        return f'{self.width}x{self.height}'

    class Meta:
        verbose_name = "размер изображения"
        verbose_name_plural = "размеры изображения"


class Picture(models.Model):
    dimensions = models.ManyToManyField(Dimension, verbose_name="размер изображения")
    picture = models.ImageField(upload_to='product/', verbose_name="изображение")

    def __str__(self):
        return f'{self.picture}'

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="подкатегория")
    picture = models.ForeignKey(Picture, on_delete=models.SET_DEFAULT, verbose_name="изображение", default=1)

    name = models.CharField(max_length=255, unique=True, verbose_name="наименование")
    slug_name = models.SlugField(max_length=255, unique=True, verbose_name="slug-имя")
    price = models.PositiveIntegerField(verbose_name="цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
