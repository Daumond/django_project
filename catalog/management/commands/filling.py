import json

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open(BASE_DIR / 'category_data.json', encoding='utf-8') as fp:
            category_data = json.load(fp)
            for item in category_data:
                Category.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"]
                )

        with open(BASE_DIR / 'product_data.json', encoding='utf-8') as fp:
            product_data = json.load(fp)
            for item in product_data:
                category_pk = item["fields"]["category"]
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"],
                    preview=item["fields"]["preview"],
                    category=category,
                    price=item["fields"]["price"],
                    created_at=item["fields"]["created_at"],
                    last_modified_date=item["fields"]["last_modified_date"]
                )
