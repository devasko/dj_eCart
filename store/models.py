from django.db import models
from category.models import Category


class Product(models.Model):
    title           = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models. TextField(max_length=500, blank=True)
    price           = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_availaible   = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
