from django.shortcuts import render
from .models import Accessory, Category


def accessories(request):
    accessories = (
        Accessory.objects
        .select_related("subcategory", "subcategory__category")
        .prefetch_related("additional_images")
        .order_by("-created_at")
    )

    categories = Category.objects.prefetch_related("subcategories").all()

    return render(request, "accessories.html", {
        "accessories": accessories,
        "categories": categories
    })
