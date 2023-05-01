## Import libraries:
import requests
from bs4 import BeautifulSoup


## List of links:
banrep_link = 'https://totoro.banrep.gov.co/estadisticas-economicas/'
dane_link = 'https://www.dane.gov.co/index.php/indicadores-economicos'
republica_link = 'https://www.larepublica.co/indicadores-economicos/macro'


## Indicators
def inflacion_anual():
    try:
        banrep = requests.get(banrep_link)
        if banrep.status_code == 200:
            banrep = BeautifulSoup(banrep.text, features='html.parser')
            inflacion_anual = banrep.find(attrs= {'id':'principalesIndicadoresContainer'}).find_all('span', attrs = {'class' : 'valor-indicador-principal'})[0].get_text()
            return inflacion_anual
        else:
            raise ValueError(f'Error: {banrep.status_code}\n in {banrep_link}')
    except ValueError as ve:
        print (ve)

def pib_trimestral():
    try:
        banrep = requests.get(banrep_link)
        if banrep.status_code == 200:
            banrep = BeautifulSoup(banrep.text, features='html.parser')
            pib_trimestral = banrep.find(attrs= {'id':'principalesIndicadoresContainer'}).find_all('span', attrs = {'class' : 'valor-indicador-principal'})[2].get_text()
            return pib_trimestral
        else:
            raise ValueError(f'Error: {banrep.status_code}\n in {banrep_link}')
    except ValueError as ve:
        print (ve)
        
def tasa_intervencion():
    try:
        banrep = requests.get(banrep_link)
        if banrep.status_code == 200:
            banrep = BeautifulSoup(banrep.text, features='html.parser')
            tasa_intervencion = banrep.find(attrs= {'id':'principalesIndicadoresContainer'}).find_all('span', attrs = {'class' : 'valor-indicador-principal'})[1].get_text()
            return tasa_intervencion
        else:
            raise ValueError(f'Error: {banrep.status_code}\n in {banrep_link}')
    except ValueError as ve:
        print (ve)

def inflacion_mensual():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            inflacion_mensual = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[1].find_all('div', attrs = {'class' : 'col-sm-4'})[1].find('h1').get_text()
            return inflacion_mensual
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)

def pib_anual():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            pib_anual = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[1].find_all('div', attrs = {'class' : 'col-sm-4'})[2].find('h1').get_text()
            return pib_anual
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)
        
def desempleo():
    try:
        dane = requests.get(dane_link)
        if dane.status_code == 200:
            dane = BeautifulSoup(dane.text, features='html.parser')
            desempleo = dane.find(attrs= {'id' : 't3-content'}).find_all('div', attrs= {'class' : 'row'})[1].find_all('div', attrs = {'class' : 'col-sm-4'})[0].find('h1').get_text()
            return desempleo
        else:
            raise ValueError(f'Error: {dane.status_code}\n in {dane_link}')
    except ValueError as ve:
        print(ve)
        
def inflacion_corrido():
    try:
        republica = requests.get(republica_link)
        if republica.status_code == 200:
            republica = BeautifulSoup(republica.text, features='html.parser')
            inflacion_corrido = republica.find_all('div', attrs= {'class' : 'd-flex m-none mb-4'})[0].find_all('div', attrs= {'class' : 'cardI anconIndicador'})[0].find('span', attrs = {'class' : 'priceIndicator'}).get_text()
            return inflacion_corrido
        else:
            raise ValueError(f'Error: {republica.status_code}\n in {republica_link}')
    except ValueError as ve:
        print(ve)