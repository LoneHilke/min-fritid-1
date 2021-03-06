#from turtle import title
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import Hobby, Kategori, SlagsModel, Kommentar, Modeller

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/about.html')   

class Slags(View):
    def get(self, request, *args, **kwargs):
        # each item form kategori
        perler = Hobby.objects.filter(kategori__titel__contains='Perler')
        knipling = Hobby.objects.filter(kategori__titel__contains='Knipling')
        filt = Hobby.objects.filter(kategori__titel__contains='Filt')  
        papir = Hobby.objects.filter(kategori__titel__contains='Papir')
      
        context = {
            'perler': perler,
            'knipling': knipling,
            'filt': filt,
            'papir': papir,
        }
        return render(request, 'fritid/slags.html', context)

    def post(self, request, *args, **kwargs):
        navn = request.POST.get('navn')
        email = request.POST.get('email')
        gade = request.POST.get('gade')
        by = request.POST.get('by')
        land = request.POST.get('land')

        slags_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            hobby_item = Hobby.objects.get(pk__contains=int(item))
            item_data = {
                'id': hobby_item.pk,
                'titel': hobby_item.titel,
                'pris': hobby_item.pris
            }

            slags_items['items'].append(item_data)

            pris = 0
            item_ids = []

        for item in slags_items['items']:
            pris += item['pris']
            item_ids.append(item['id'])

        slags = SlagsModel.objects.create(
            pris=pris,
            navn=navn,
            email=email,
            gade=gade,
            by=by,
            land=land,
            )

        slags.items.add(*item_ids)

        body = ('Tak for din ordrer. Jeg vil g?? igang s?? hurtigt som muligt, og du vil modtage en mail, n??r det er klart.\n'
         'Betaling foreg??r via Mobilpay. ' f'Din pris er: {pris}\n')

        send_mail(
            'Tak for din ordrer.',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': slags_items['items'],
            'pris': pris
        }

        return redirect('slags-confirmation', pk=slags.pk)

class Perler(View):
    def get(self, request, *args, **kwargs):

        perler = Hobby.objects.filter(kategori__titel__contains='Perler')

        context = {
            'perler': perler
        }
        return render(request, 'fritid/perler.html', context)

class Kniplinger(View):
    def get(self, request, *args, **kwargs):

        knipling = Hobby.objects.filter(kategori__titel__contains='Knipling')

        context = {
            'knipling': knipling
        }
        return render(request, 'fritid/kniplinger.html', context)

class Filt(View):
    def get(self, request, *args, **kwargs):

        filt = Hobby.objects.filter(kategori__titel__contains='Filt')  

        context = {
            'filt': filt
        }
        return render(request, 'fritid/filt.html', context)

class Papir(View):
    def get(self, request, *args, **kwargs):

        papir = Hobby.objects.filter(kategori__titel__contains='Papir')

        context = {
            'papir': papir
        }
        return render(request, 'fritid/papir.html', context)

class SlagsConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        slags = SlagsModel.objects.get(pk=pk)

        context = {
            'pk': slags.pk,
            'items': slags.items,
            'pris': slags.pris
        }

        return render(request, 'fritid/slags_confirmation.html', context)

class Start(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/start.html')

class Test(View):
    def get(self, request, *args, **kwargs):
        # each item form kategori
        
        perler = Modeller.objects.filter(emne__name__contains='Perler')  
        knipling = Modeller.objects.filter(emne__name__contains='Knipling')
        filt = Modeller.objects.filter(emne__name__contains='Filt')
        papir = Modeller.objects.filter(emne__name__contains='Papir')
         
        context = {
            'perler': perler,
            'knipling': knipling,
            'filt': filt,
            'papir': papir,
        }
        
        return render(request, 'fritid/test.html', context)

class Kategorier(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fritid/kategorier.html')












# fra: https://www.youtube.com/watch?v=QEnY1lLcd1E&list=PLPSM8rIid1a0qiCpbfujex5lZoXr2SRFC&index=3