from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, SubCategory, Car


def catalog(request):
    """
    Каталог всех автомобилей с фильтрацией по категориям и поиском
    """
    # Получаем все категории с подсчетом количества автомобилей
    categories = Category.objects.prefetch_related('subcategories').all()
    
    # Аннотируем категории количеством автомобилей
    for category in categories:
        car_count = 0
        for subcategory in category.subcategories.all():
            car_count += subcategory.cars.count()
        category.accessories_count = car_count
    
    # Получаем параметры фильтрации
    selected_category = request.GET.get('category')
    selected_subcategory = request.GET.get('subcategory')
    search_query = request.GET.get('q', '').strip()
    
    # Начинаем с всех автомобилей
    cars = Car.objects.select_related('subcategory__category').all()
    
    # Применяем фильтры
    if selected_category:
        cars = cars.filter(subcategory__category_id=selected_category)
    
    if selected_subcategory:
        cars = cars.filter(subcategory_id=selected_subcategory)
    
    # Применяем поиск
    if search_query:
        cars = cars.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(subcategory__name__icontains=search_query) |
            Q(subcategory__category__name__icontains=search_query)
        )
    
    # Сортировка по дате создания (сначала новые)
    cars = cars.order_by('-created_at')
    
    context = {
        'cars': cars,  # Используем 'cars' вместо 'accessories'
        'categories': categories,
        'selected_category': selected_category,
        'selected_subcategory': selected_subcategory,
        'q': search_query,
    }
    
    return render(request, 'catalog.html', context)


def car_detail(request, car_id):
    """
    Детальная страница автомобиля
    """
    car = get_object_or_404(
        Car.objects.select_related('subcategory__category')
                    .prefetch_related('additional_images'),
        id=car_id
    )
    
    # Получаем связанные автомобили (из той же подкатегории)
    related_cars = Car.objects.filter(
        subcategory=car.subcategory
    ).exclude(
        id=car.id
    ).order_by('-created_at')[:4]  # Берем 4 последних
    
    context = {
        'car': car,  # Используем 'car' вместо 'accessory'
        'related': related_cars,
    }
    
    return render(request, 'details.html', context)