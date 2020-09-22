import codecs
import os, sys

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, Programming_language

parsers = (
    (tut_by, 'https://jobs.tut.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=Python'),
    (trudbox, 'http://trudbox.by/minsk?whatQuery=Python+')
)

city = City.objects.filter(slug='minsk')
a = 1
jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()
