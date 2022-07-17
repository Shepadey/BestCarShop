from django.contrib import admin
from core.models import Example
@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ("name","color","cost")
    search_fields = ("color","cost","name")

# Register your models here.
