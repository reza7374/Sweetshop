from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=160,unique=True)
    descritption = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=255, blank=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"Image for {self.product.name}"
