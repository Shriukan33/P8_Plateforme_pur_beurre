from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    """Represents a product from OpenFoodFacts"""

    product_name = models.CharField(max_length=200)
    product_url = models.URLField(max_length=200)
    product_image = models.URLField(max_length=200)
    product_nutriscore = models.CharField(max_length=1)
    product_category = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"


class Favorites(models.Model):
    """Represents a favorite product"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('product_lookup.Products',
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoris"
