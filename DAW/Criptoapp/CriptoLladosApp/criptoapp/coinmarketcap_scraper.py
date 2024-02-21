
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd


url = 'https://coinmarketcap.com/new/'
service = Service(executable_path=r'./chromedriver')
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1200")
browse = webdriver.Chrome(service=service, options=chrome_options)
browse.get(url)

table_wrap = WebDriverWait(browse, 5).until(EC.presence_of_element_located((By.CLASS_NAME,
"sc-14cb040a-2.dGwknr")))
tables = table_wrap.find_elements(By.XPATH, ".//table")
print(tables)
table_gainers = tables[0]

"""rows = table_gainers.find_elements(By.XPATH, ".//tbody/tr")
for row in rows:
    cells = row.find_elements(By.XPATH, ".//td")
    row_text = (cells[1].text + ' - ' + cells[2].text)
    print(row_text)"""

table_gainers_bs = BeautifulSoup(table_gainers.get_attribute('outerHTML'), 'html.parser')
dataframe = pd.read_html(str(table_gainers_bs))[0]
print(dataframe)

name = dataframe["Name"].astype('string')
price = dataframe["Price"].str.strip("$")
dataframe.insert(loc = 5, column = "Price(float)", value = price)
dataframe = dataframe.drop(columns=["Price"])
dataframe = dataframe.drop(columns=["1h"])
dataframe = dataframe.drop(columns=["24h"])
dataframe = dataframe.drop(columns=["Fully Diluted Market Cap"])
dataframe = dataframe.drop(columns=["Volume"])
dataframe = dataframe.drop(columns=["Blockchain"])
dataframe = dataframe.drop(columns=["Added"])
dataframe = dataframe.drop(columns=["Unnamed: 0"])
dataframe = dataframe.drop(columns=["#"])
print(price)
print(dataframe)

"""import sqlite3
conn = sqlite3.connect("ruta_al_fichero/output.sqlite")
cur = conn.cursor()
...
for item in collected_items:
    cur.execute("INSERT INTO scraped_data (nombre, precio, fecha_creacion) values (?, ?, ?)",
    (item["title"], item["price"], item["url"])
    )"""

