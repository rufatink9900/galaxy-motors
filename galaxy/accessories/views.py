from django.shortcuts import render, get_object_or_404
from .models import Accessory, Category
from django.db.models import Q

def accessories(request):
    q = request.GET.get("q", "").strip()
    category_id = request.GET.get("category")
    subcategory_id = request.GET.get("subcategory")

    accessories_qs = (
        Accessory.objects
        .select_related("subcategory", "subcategory__category")
        .prefetch_related("additional_images")
        .order_by("-created_at")
    )

    # 🔎 Search
    if q:
        accessories_qs = accessories_qs.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )

    # 🎯 Filter by category
    if category_id:
        accessories_qs = accessories_qs.filter(subcategory__category_id=category_id)

    # 🎯 Filter by subcategory
    if subcategory_id:
        accessories_qs = accessories_qs.filter(subcategory_id=subcategory_id)

    categories = (
        Category.objects
        .prefetch_related("subcategories")
        .all()
        .order_by("name")
    )

    return render(request, "accessories.html", {
        "accessories": accessories_qs,
        "categories": categories,
        "q": q,
        "selected_category": category_id,
        "selected_subcategory": subcategory_id,
    })



def accessory_detail(request, pk):
    accessory = get_object_or_404(
        Accessory.objects.select_related("subcategory", "subcategory__category")
        .prefetch_related("additional_images"),
        pk=pk
    )

    # похожие аксессуары (в той же подкатегории)
    related = (
        Accessory.objects
        .filter(subcategory=accessory.subcategory)
        .exclude(pk=accessory.pk)
        .select_related("subcategory", "subcategory__category")
        .order_by("-created_at")[:6]
    )

    return render(request, "accessory_detail.html", {
        "accessory": accessory,
        "related": related
    })
