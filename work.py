import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }


def tut_by(url):
    jobs = []
    errors = []
    domain = 'https://jobs.tut.by'
    url = 'https://jobs.tut.by/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text=Python'
    resp = requests.get(url, headers=headers)
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
                print(company_name)
                jobs.append({'title': title.text, 'url': domain + href, 'description': text1 + text2,
                             'company': company_name})
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not exist'})
    return jobs, errors


def belmeta(url):
    jobs = []
    errors = []
    domain = 'https://belmeta.com'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find_all('div', class_='jobs')
        if main_div:
            for div in main_div:
                title = div.find('a')
                href = title.get('href')
        else:
            errors.append({'url': url, 'title': 'Div does not exists'})
    else:
        errors.append({'url': url, 'title': 'Page do not exist'})
    return jobs, errors

if __name__ == '__main__':
    url = 'https://belmeta.com/vacansii?q=Python&l=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA'
    jobs, errors = belmeta(url)
    # h = codecs.open('work.txt', 'w', 'utf-8')
    # h.write(str(jobs))
    # h.close()
    # print(div_list)
