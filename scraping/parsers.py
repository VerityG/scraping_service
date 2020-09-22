import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('tut_by', 'trudbox')

headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
           'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:80.0) Gecko/20100101 Firefox/80.0',
           'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
           ]


def tut_by(url):
    jobs = []
    errors = []
    url = 'https://jobs.tut.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=Python'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', class_='vacancy-serp')
        if main_div:
            div_list = main_div.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
            for div in div_list:
                title = div.find('a', class_="bloko-link HH-LinkModifier")
                href = title.get('href')
                content1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
                text1 = content1.get_text()
                content2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'})
                text2 = content2.get_text()
                company = div.find('div', attrs={'class': 'vacancy-serp-item__meta-info'})
                company_name = company.get_text()
                jobs.append({'title': title.text, 'url': href, 'description': text1 + text2,
                             'company': company_name})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not exist'})

    return jobs, errors


def trudbox(url):
    jobs = []
    errors = []
    url = 'http://trudbox.by/minsk?whatQuery=Python+'
    resp = requests.get(url, headers=headers[randint(0, 2)])
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', class_='row content')
        if main_div:
            div_list = main_div.find_all('div', attrs={'itemtype': True})
            for div in div_list:
                job_title = div.find('div', attrs={'itemprop': 'title'})
                title = job_title.get_text()
                link = div.find('div', attrs={'data-href': True})
                href = link.get('data-href')
                content = div.find('div', attrs={'itemprop': 'description'})
                text = content.get_text()
                company = div.find('span', attrs={'itemprop': 'hiringOrganization'})
                company_name = company.get_text()
                a = 1
                jobs.append({'title': title, 'url': href, 'description': text,
                                 'company': company_name})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not exist'})

    return jobs, errors


if __name__ == '__main__':
    jobs, errors = trudbox()
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
