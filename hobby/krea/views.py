from django.shortcuts import render
from django.views import View
from .models import Modeller, Kategori

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        perler = Modeller.objects.filter(
            kategori__titel__contains='Perler'
            )
        knipling = Modeller.objects.filter(
            kategori__titel__contains='Knipling'
        )
        filt = Modeller.objects.filter(
            kategori__titel__contains='Filt'
        )
        papir =Modeller.objects.filter(
            kategori__titel__contains='Papir'
        )

        context = {
            'perler': perler,
            'knipling': knipling,
            'filt': filt,
            'papir': papir,
        }
        #return render(request, 'fritid/slags.html', context)
        return render(request, 'krea/dashboard.html', context)

