from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from  core.views import main
urlpatterns = [
    path("", main, name='main'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
