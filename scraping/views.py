from django.shortcuts import render
from .forms import FindForm
from .models import Vacancy


def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    programming_language = request.GET.get('programming_language')
    qs = []
    if city or programming_language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if programming_language:
            _filter['programming_language__slug'] = programming_language

        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'scraping/home.html', {'object_list': qs, 'form': form})
