from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)

    class Meta:
        unique_together = ("category", "name")  # чтобы не было одинаковых подкатегорий в одной категории

    def __str__(self):
        return f"{self.category.name}  {self.name}"


class Car(models.Model):
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="cars",
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    main_image = CloudinaryField("main_image", blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subcategory.category.name} -> {self.subcategory.name} -> {self.name}"


class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        related_name="additional_images",
        on_delete=models.CASCADE
    )
    image = CloudinaryField("image")

    def __str__(self):
        return f"{self.car.name} image"
