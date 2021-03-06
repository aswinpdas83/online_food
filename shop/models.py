from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse()

    def __str__(self):
        return self.slug


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    product_image = models.ImageField(upload_to='pictures')
    desc = models.TextField(max_length=1000)
    product_price = models.FloatField()
    stock = models.IntegerField()
    available = models.BooleanField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
