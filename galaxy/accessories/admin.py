from django.contrib import admin
from .models import Category, SubCategory, Accessory, AccessoryImage


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


class AccessoryImageInline(admin.TabularInline):
    model = AccessoryImage
    extra = 1


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category_name", "subcategory", "price", "created_at")
    list_filter = ("subcategory__category", "subcategory", "created_at")
    search_fields = ("name", "description", "subcategory__name", "subcategory__category__name")
    autocomplete_fields = ("subcategory",)
    inlines = [AccessoryImageInline]
    ordering = ("-created_at",)

    def category_name(self, obj):
        return obj.subcategory.category.name
    category_name.short_description = "Category"


@admin.register(AccessoryImage)
class AccessoryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "accessory")
    search_fields = ("accessory__name",)
    autocomplete_fields = ("accessory",)

exclude = ("name", "description")