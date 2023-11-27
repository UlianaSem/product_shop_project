from django.core.management import BaseCommand

from shop.models import Dimension, Picture


class Command(BaseCommand):

    DIMENSIONS = ((100, 100), (250, 250), (500, 500))

    def handle(self, *args, **options):
        for dimensions in self.DIMENSIONS:
            Dimension.objects.create(height=dimensions[0], width=dimensions[1])

        picture = Picture.objects.create()
        picture.picture = 'product/empty.png'
        picture.dimensions.set(Dimension.objects.filter(pk__in=[1, 2, 3]))
        picture.save()
