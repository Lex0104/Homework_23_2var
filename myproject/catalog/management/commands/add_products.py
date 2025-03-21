from django.core.management.base import BaseCommand
from django.core.management import call_command
from .models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the DB'

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories = call_command('loaddata', 'category_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
        products = call_command('loaddata', 'product_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))