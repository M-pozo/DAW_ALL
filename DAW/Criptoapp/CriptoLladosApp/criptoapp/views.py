# En views.py de tu aplicación Django

from bs4 import BeautifulSoup
from django.shortcuts import render
from pandas import DataFrame
from .models import Criptomoneda
from .utils import extraer_criptomonedas

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Criptomoneda
from datetime import datetime
import pandas as pd
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

def listar_criptomonedas(request):
    url = 'https://coinmarketcap.com/new/'
    service = Service(executable_path=r'./chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1200")
    browse = webdriver.Chrome(service=service, options=chrome_options)
    browse.get(url)

    table_wrap = WebDriverWait(browse, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"sc-14cb040a-2.dGwknr")))
    tables = table_wrap.find_elements(By.XPATH, ".//table")
    table_gainers = tables[0]

    """rows = table_gainers.find_elements(By.XPATH, ".//tbody/tr")
    for row in rows:
        cells = row.find_elements(By.XPATH, ".//td")
        row_text = (cells[1].text + ' - ' + cells[2].text)
        print(row_text)"""

    table_gainers_bs = BeautifulSoup(table_gainers.get_attribute('outerHTML'), 'html.parser')
    dataframe = pd.read_html(str(table_gainers_bs))[0]

    #Modificar columna
    price = dataframe["Price"].str.strip("$")
    #Insertar columna
    dataframe.insert(loc= 5, column= "Price(float)", value= price)
    #Eliminar columnas
    dataframe = dataframe.drop(columns=["#"])
    dataframe = dataframe.drop(columns=["Unnamed: 0"])
    dataframe = dataframe.drop(columns=["Price"])
    dataframe = dataframe.drop(columns=["1h"])
    dataframe = dataframe.drop(columns=["24h"])
    dataframe = dataframe.drop(columns=["Fully Diluted Market Cap"])
    dataframe = dataframe.drop(columns=["Volume"])
    dataframe = dataframe.drop(columns=["Blockchain"])
    dataframe = dataframe.drop(columns=["Added"])
    #print(dataframe)
    
    posicion = 0
    while (posicion >= len(dataframe)):
        posicion+=1
        if '...' in dataframe['Price(float)'][posicion] or ',' in dataframe['Price(float)'][posicion]:
            continue
        if not Criptomoneda.objects.filter(nombre=dataframe['Name'][posicion]).exists():
            date = datetime.now()
            Criptomoneda.objects.create(nombre=dataframe['Name'][posicion], 
                                        precio=dataframe['Price(float)'][posicion], 
                                        fecha_creacion=date
                                        )
    #Cierra el navegador
    browse.quit()
    #
    criptomonedas = Criptomoneda.objects.all()
    return render(request, 'listar_criptomonedas.html', {'criptomonedas': criptomonedas})
