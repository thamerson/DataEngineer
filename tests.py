import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup

def obterConteudo(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")
    options.add_argument("--disable-web-security")

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.get(url)
    
    # Imitando um comportamento humano com pausa aleatória
    time.sleep(random.randint(10, 20))
    
    conteudo = navegador.find_element(By.XPATH, '/html/body').get_attribute('innerHTML')

    
    return conteudo

# Restante do código ...

def main():
    conteudo = obterConteudo('https://steamdb.info/sales/')
    soup = BeautifulSoup(conteudo, "html.parser")
    tables = soup.find_all('table')
    
    dfs = []
    
    for i, table in enumerate(tables):
        df = pd.read_html(str(table))[0]
        dfs.append(df)
        df.to_csv(f'dados_tabela_{i}.csv', index=False)

if __name__=="__main__":
    main()
