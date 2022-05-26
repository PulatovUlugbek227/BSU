from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('MikeW/', admin.site.urls),
    path('', include('zones.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
