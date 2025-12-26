
from django.shortcuts import render, get_object_or_404
from .models import Service, Category, SubCategory

def services(request, category_id=None, subcategory_id=None):
    # Получаем все категории
    categories = Category.objects.all()

    # Если выбрана категория
    active_category = None
    active_subcategory = None
    subcategories = []

    services_list = Service.objects.filter(is_active=True).select_related('subcategory__category')

    if category_id:
        active_category = category_id
        services_list = services_list.filter(subcategory__category_id=category_id)
        subcategories = SubCategory.objects.filter(category_id=category_id)

    if subcategory_id:
        active_subcategory = subcategory_id
        services_list = services_list.filter(subcategory_id=subcategory_id)

    context = {
        'services': services_list,
        'categories': categories,
        'subcategories': subcategories,
        'active_category': active_category,
        'active_subcategory': active_subcategory
    }
    return render(request, 'services.html', context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk, is_active=True)
    similar_services = Service.objects.filter(
        subcategory=service.subcategory
    ).exclude(pk=service.pk)[:3]
    context = {
        'service': service,
        'similar_services': similar_services,
    }
    return render(request, 'service_detail.html', context)
