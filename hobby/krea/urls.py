#from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)