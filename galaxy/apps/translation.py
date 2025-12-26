from modeltranslation.translator import register, TranslationOptions
from .models import App


@register(App)
class AppTranslationOptions(TranslationOptions):
    fields = ('description',)
