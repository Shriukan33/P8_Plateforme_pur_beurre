import requests
from django.core.management.base import BaseCommand
from product_lookup.models import Products


class Command(BaseCommand):
    help = 'Builds the database'

    def handle(self, *args, **options):
        """Retrieves products from OpenFoodFacts and saves them
        in the database."""
        products = self.get_products()
        self.save_products(products)

    def get_products(self, *args) -> dict:
        """
        Returns France's top 500 most popular products
        ordered by scan on OpenFoodFacts.
        """
        print('Fetching France\'s top 500 most popular '
              'products on OpenFoodFacts...')
        url = ("https://fr.openfoodfacts.org/cgi/search.pl?action=process"
               "&sort_by=popularity&page_size=500&page=1&"
               "sort_by=unique_scans_n&"
               "fields=product_name,nutriscore_grade,url,categories,"
               "pnns_groups_1,pnns_groups_2,image_url&"
               "coutries=france&json=true")

        response = requests.get(url)
        data = response.json()
        products = data['products']

        return products

    def save_products(self, products: dict):
        """
        Save a product in the database.

        The product must be a dict containing the following fields:

        product_name: str
        product_url: str -> url for OpenFoodFacts product's page.
        product_image: str -> url for OpenFoodFacts product's image.
        product_nutriscore: str
        pnns_groups_1: str

        pnns_groups_1 is a global group of product, i.e a bottle of
        water is in the "Beverages" pnns_groups_1 group.
        """
        print('Saving products in the database...')
        error_list = []
        for index, product in enumerate(products):
            print("Saving product {}/{}...".format(
                index + 1, len(products)),
                end='\r')
            try:
                product_name = product['product_name']
                product_url = product['url']
                product_image = product['image_url']
                product_nutriscore = product['nutriscore_grade']
                product_category = product['pnns_groups_1']

                product_obj = Products(
                    product_name=product_name,
                    product_url=product_url,
                    product_image=product_image,
                    product_nutriscore=product_nutriscore,
                    product_category=product_category
                )
                product_obj.save()
            except KeyError as e:
                error_list.append(
                    "- {} is missing : {} - Dropped the item".format(
                        product["product_name"], e))
                continue
        print("\n".join(error_list))
        print(len(products)-len(error_list), "products saved.")