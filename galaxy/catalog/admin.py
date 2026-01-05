from django.contrib import admin
from .models import Category, SubCategory, Car, CarImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
    autocomplete_fields = ("category",)


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category_name", "subcategory", "price", "created_at")
    list_filter = ("subcategory__category", "subcategory", "created_at")
    search_fields = ("name", "description", "subcategory__name", "subcategory__category__name")
    autocomplete_fields = ("subcategory",)
    inlines = [CarImageInline]
    ordering = ("-created_at",)

    # ⚠️ если используешь modeltranslation и хочешь показывать name_ru / description_ru и т.д.
    # то можешь оставить exclude, а если НЕ используешь modeltranslation — УБЕРИ exclude
    exclude = ("name", "description")

    def category_name(self, obj):
        return obj.subcategory.category.name

    category_name.short_description = "Category"


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ("id", "car")
    search_fields = ("car__name",)
    autocomplete_fields = ("car",)
