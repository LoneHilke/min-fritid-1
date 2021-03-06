"""hobby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from fritid.views import Index, About, Slags, SlagsConfirmation, Start, Test, Kategorier, Perler, Kniplinger, Filt, Papir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('krea/', include('krea.urls')),
    path('', Index.as_view(), name='index'),
    path('about', About.as_view(), name='about'),
    path('start', Start.as_view(), name='start'),
    path('slags/', Slags.as_view(), name='slags'),
    path('test', Test.as_view(), name='test'),
    path('kategorier', Kategorier.as_view(), name='kategorier'),
    path('perler', Perler.as_view(), name='perler'),
    path('kniplinger', Kniplinger.as_view(), name='kniplinger'),
    path('filt', Filt.as_view(), name='filt'),
    path('papir', Papir.as_view(), name='papir'),
    path('slags-confirmation/<int:pk>', SlagsConfirmation.as_view(), name='slags-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
