from django.contrib import admin
from .models import Hobby, Kategori, SlagsModel, Kommentar, Modeller, Emne


# Register your models here.
admin.site.register(Hobby)
admin.site.register(Kategori)
admin.site.register(SlagsModel)
admin.site.register(Kommentar)
admin.site.register(Modeller)
admin.site.register(Emne)