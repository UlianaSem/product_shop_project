from rest_framework.serializers import ModelSerializer, SerializerMethodField

from shop.models import Category, SubCategory, Product


class SubCategorySerializer(ModelSerializer):
    class Meta:
        fields = ['name', 'slug_name', 'picture']
        model = SubCategory


class CategorySerializer(ModelSerializer):
    subcategory = SubCategorySerializer(many=True)

    class Meta:
        fields = ['name', 'slug_name', 'picture', "subcategory"]
        model = Category


class ProductSerializer(ModelSerializer):
    subcategory = SerializerMethodField()
    category = SerializerMethodField(read_only=True)

    class Meta:
        fields = ['name', 'slug_name', 'picture', "category", "subcategory", "price"]
        model = Product

    def get_subcategory(self, instance):
        return SubCategory.objects.get(pk=instance.subcategory.pk).name

    def get_category(self, instance):
        return Category.objects.get(pk=SubCategory.objects.get(pk=instance.subcategory.pk).category.pk).name
