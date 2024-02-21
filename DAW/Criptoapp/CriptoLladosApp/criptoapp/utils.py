
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Criptomoneda
from datetime import datetime

def extraer_criptomonedas():
    url = 'https://coinmarketcap.com/en/'
    service = Service(executable_path=r'./chromedriver.exe')
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1200")
    browse = webdriver.Chrome(service=service, options=chrome_options)
    browse.get(url)

    div = WebDriverWait(browse, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-14cb040a-2.hptPYH")))
    table = div.find_element(By.CLASS_NAME, "sc-14cb040a-3.dsflYb.cmc-table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    columnas = tbody.find_elements(By.TAG_NAME, "tr")

    for columna in columnas:
        cells = columna.find_elements(By.TAG_NAME, "td")

        name = cells[2].text
        price = cells[3].text
        fecha_actual = datetime.now()

        if not Criptomoneda.objects.filter(name=name).exists():
            Criptomoneda.objects.create(name=name, price=price, date_added=fecha_actual)

    browse.quit()