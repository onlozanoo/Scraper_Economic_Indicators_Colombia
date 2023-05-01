## Import libraries:
import requests
from bs4 import BeautifulSoup


## List of links:
banrep_link = 'https://totoro.banrep.gov.co/estadisticas-economicas/'
dane_link = 'https://www.dane.gov.co/index.php/indicadores-economicos'

## Indicators

def ibr_overnight():
    try:
        banrep = requests.get(banrep_link)
        if banrep.status_code == 200:
            banrep = BeautifulSoup(banrep.text, features='html.parser')
            ibr_overnight = banrep.find(attrs= {'id':'principalesIndicadoresContainer'}).find_all('span', attrs = {'class' : 'valor-indicador-principal'})[3].get_text()
            return ibr_overnight
        else:
            raise ValueError(f'Error: {banrep.status_code}\n in {banrep_link}')
    except ValueError as ve:
        print (ve)

def uvr():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            uvr = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[0].find_all('div', attrs = {'class' : 'col-sm-4'})[1].find('h1').get_text() 
            return uvr 
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)

def dtf():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            dtf = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[0].find_all('div', attrs = {'class' : 'col-sm-4'})[2].find('h1').get_text()  
            return dtf
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)
