from django.contrib import admin
from django import forms
from .models import App

class AppAdminForm(forms.ModelForm):
    apk_upload = forms.FileField(required=False, label="Upload APK")

    class Meta:
        model = App
        fields = ['name', 'description', 'apk_upload']

    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_file = self.cleaned_data.get('apk_upload')
        if uploaded_file:
            instance.apk_file = uploaded_file.read()
            instance.apk_filename = uploaded_file.name
        if commit:
            instance.save()
        return instance

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    form = AppAdminForm
    list_display = ('name', 'description', 'apk_filename')
