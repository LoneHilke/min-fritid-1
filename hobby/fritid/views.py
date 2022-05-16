from django.shortcuts import render
from django.views import View
from .models import Hobby, Kategori, SlagsModel, Kommentar

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/index.html',)

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/about.html',)   

class Slags(View):
    def get(self, request, *args, **kwargs):
        # each item form kategori
        perler =Hobby.objects.filter(kategori__titel__contains='Perler'
        )
        knipling = Hobby.objects.filter(
            kategori__titel__contains='Knipling'
        )
        filt = Hobby.objects.filter(
            kategori__titel__contains='Filt'
        )
        papir =Hobby.objects.filter(
            kategori__titel__contains='Papir'
        )

        context = {
            'perler': perler,
            'knipling': knipling,
            'filt': filt,
            'papir': papir,
        }
        return render(request, 'fritid/slags.html', context)


