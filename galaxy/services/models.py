from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    # Car Brand / Manufacturer (e.g., Changan, Tesla, BYD)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    # Car Model (e.g., CS55 Plus, UNI-K)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="models"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        unique_together = ("category", "slug")

    def __str__(self):
        return f"{self.category.name} — {self.name}"


class Service(models.Model):
    # Car Service (e.g., Oil Change, Tire Replacement)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name="services",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = CloudinaryField(
        'image',
        folder='services',
        blank=True,
        null=True
    )
    price = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title
