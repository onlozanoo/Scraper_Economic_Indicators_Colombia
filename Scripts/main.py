## Import Libraries
import monetary
import financial
import exchange_rate
import os
import datetime
import csv




def indicator(today):
    os.chdir('F:\Documentos\Proyectos DS\Web_Scraper-Economic-Indicators-Colombia\Results')
    with open('{}.csv'.format(today), 'w', encoding= 'utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        
        writer.writerow(['Indicadores Cambiarios'])
        
        writer.writerow(['Inflacion Anual', monetary.inflacion_anual(), 'Banrep'])
        writer.writerow(['PIB Trimestral', monetary.pib_trimestral(), 'Banrep'])
        writer.writerow(['PIB Anual', monetary.pib_anual(), 'Dane'])
        writer.writerow(['Tasa de Intervencion', monetary.tasa_intervencion(), 'Banrep'])
        writer.writerow(['Inflacion Mensual', monetary.inflacion_mensual(), 'Dane'])
        writer.writerow(['Inflacion Ano Corrido', monetary.inflacion_corrido(), 'La Republica'])
        writer.writerow(['Desempleo', monetary.desempleo(), 'Dane'])
        
        writer.writerow(['Indicadores Financieros'])
        
        writer.writerow(['IBR Overnight', financial.ibr_overnight(), 'Banrep'])
        writer.writerow(['UVR', financial.uvr(), 'Dane'])
        writer.writerow(['DTF(ea)', financial.dtf(), 'Dane'])
        
        writer.writerow(['Indicadores Cambiarios'])
        
        writer.writerow(['Petroleo WTI', exchange_rate.wti(), 'Dane'])
        writer.writerow(['TRM', exchange_rate.trm(), 'Banrep'])
        writer.writerow(['Cuenta Corriente Trimestral', exchange_rate.cuenta_corriente(), 'Banrep'])



def today_file(**today):
    today = datetime.date.today().strftime('%d-%m-%Y')
    indicator(today)

def run():
    today_file()
    
if __name__ == '__main__':
    run()