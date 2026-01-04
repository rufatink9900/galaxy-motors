from modeltranslation.translator import register, TranslationOptions
from .models import Accessory


@register(Accessory)
class AccessoryTranslationOptions(TranslationOptions):
    fields = ("name", "description")
