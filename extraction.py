from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np

driver = webdriver.Chrome(executable_path="C:\\Users\\danbl\\Instituto CPE\\Webinars\\py_power_bi\\Pag\\chromedriver.exe")
driver.get('https://danblanc.github.io/pag_webinar/')
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')

comentarios = soup.find_all("div", class_ = "card")

usuarios = []
rates = []
descripcion = []
fechas = []

for comentario in comentarios:
    usuarios.append(comentario.find("b"))
    rates.append(len(comentario.find_all("span", class_= "checked")))
    descripcion.append(comentario.find("p").text)
    if len(comentario.find_all("span")) > 0:
        fechas.append(comentario.find_all("span")[-1].text)
    else:
        fechas.append("Error")

coments = pd.DataFrame(list(zip(usuarios, rates, descripcion, fechas)), 
                        columns = ["usuarios", "rates", "descripcion", "fechas"] )      

coments = coments.iloc[1:,:]
coments.rates = coments.rates.astype(int)
coments.fechas = pd.to_datetime(coments.fechas, format = "%d/%m/%Y").dt.date     

"""
coments["result"] = np.where(
    coments.rates == 3,
    "Neutro",
    np.where(coments.rates < 3,
    "Negativo", 
    "Positivo"))
"""

driver.quit()