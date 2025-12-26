from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, SubCategory, Service

# Category без перевода
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

# SubCategory без перевода
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {"slug": ("name",)}

# Service с переводом
@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'subcategory', 'is_active')
    list_filter = ('subcategory', 'is_active')
    search_fields = ('title', 'description')

# Настройка заголовков админки
admin.site.site_header = "Galaxy Motors Admin"
admin.site.site_title = "Galaxy Motors Portal"
admin.site.index_title = "Добро пожаловать в админку"
