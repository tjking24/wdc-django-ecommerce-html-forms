from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from products.models import Category, Product, ProductImage
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Imports initial data'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        ProductImage.objects.all().delete()

        User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin')

        CATEGORIES = [
            'Shoes', 'Accessories', 'Clothing'
        ]
        categories = []
        for category in CATEGORIES:
            c = Category.objects.create(name=category)
            categories.append(c)

        PRODUCTS = [
            ('Nike Vapor', '44444444', categories[0], 129.99),
            ('Nike Cap', '33333333', categories[1], 27.99),
            ('Diamond Necklace', '88888888', categories[1], 233),
            ('Sweater', '55555555', categories[2], 49.99),
        ]
        products = []
        for name, sku, category, price in PRODUCTS:
            p = Product.objects.create(
                name=name,
                sku=sku,
                category=category,
                price=price
            )
            products.append(p)

        IMAGES = [
            'https://images-na.ssl-images-amazon.com/images/I/61toIdeEdZL._UX695_.jpg',
            'https://images-na.ssl-images-amazon.com/images/I/61-Rm5tfPML._UX679_.jpg',
            'https://images-na.ssl-images-amazon.com/images/I/61x3zjjiDsL._UY695_.jpg',
            'https://images-na.ssl-images-amazon.com/images/I/51DtYxTRVfL._SX679._SX._UX._SY._UY_.jpg'
        ]
        for index, image in enumerate(IMAGES):
            ProductImage.objects.create(
                product=products[index],
                url=image
            )
        print('Imported!')
