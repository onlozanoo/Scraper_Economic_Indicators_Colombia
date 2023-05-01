## Import libraries:
import requests
from bs4 import BeautifulSoup


## List of links:
banrep_link = 'https://totoro.banrep.gov.co/estadisticas-economicas/'
dane_link = 'https://www.dane.gov.co/index.php/indicadores-economicos'
republica_link_2 = 'https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar'

## Indicators

def wti():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            wti = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[2].find_all('div', attrs = {'class' : 'col-sm-4'})[2].find('h1').get_text()  
            return wti
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)

def trm():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            trm = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[0].find_all('div', attrs = {'class' : 'col-sm-4'})[0].find('h1').get_text()  
            return trm
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)

def cuenta_corriente():
    try:
        banrep = requests.get(banrep_link)
        if banrep.status_code == 200:
            banrep = BeautifulSoup(banrep.text, features='html.parser')
            cuenta_corriente = banrep.find(attrs= {'id':'principalesIndicadoresContainer'}).find_all('span', attrs = {'class' : 'valor-indicador-principal'})[4].get_text()
            return cuenta_corriente
        else:
            raise ValueError(f'Error: {banrep.status_code}\n in {banrep_link}')
    except ValueError as ve:
        print (ve)
