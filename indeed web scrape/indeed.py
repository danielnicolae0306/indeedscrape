from turtle import title
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    url=f'https://ro.indeed.com/jobs?q=java&l=Bucure%C8%99ti,%20Ilfov&vjk=8089b14478ee0271&start={page}'
    req = requests.get(url,agent)
    soup = BeautifulSoup(req.content,'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div',class_ = 'job_seen_beacon')
    for item in divs:
        title = item.find('h2', class_ ="jobTitle").text.strip()
        compania = item.find('span', class_ ='companyName').text.strip()
        try:
            salariu = item.find('span',class_ ='salaryTest' ).text.strip()
        except:
            salariu = ''
        
        rezumat  = item.find('div',  {'class' : 'job-snippet'}).text.strip().replace('\n', '')
     

        job = {
            'title':title,
            'compania':compania,
            'salariu':salariu,
            'rezumat':rezumat

        }
        listajob.append(job)

    return




listajob = []

for i in range(0,40,10):
    print(f'Getting page, {i}')
    exc = extract(0)
    transform(exc)

df = pd.DataFrame(listajob)

print(df.head())

df.to_csv('jobs.csv')
