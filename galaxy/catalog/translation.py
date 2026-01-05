from modeltranslation.translator import register, TranslationOptions
from .models import Car


@register(Car)
class AccessoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")
