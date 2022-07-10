from django.contrib import admin
from core.models import Example
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

# Register your models here.
