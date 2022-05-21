from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from fritid.models import SlagsModel, Kategori

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        slags = SlagsModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day
        )

        total_revenue = 0
        for slags in slags:
            total_revenue += slags.pris

        context = {
            'slags': slags,
            'total_revenue': total_revenue,
            'total_slags': len(slags)
        }

        return render(request, 'krea/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='fritid').exists()

