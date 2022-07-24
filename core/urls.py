from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from  core.views import main,form, get_items, search_items
urlpatterns = [
    path("", main, name='main'),
    path("form", form, name='form'),
    path("get-items",get_items,name="get-items" ),
    path("search-items",search_items,name="search-items"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
