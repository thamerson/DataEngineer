import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def obterConteudo(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.get(url)

    time.sleep(5)
    conteudo = navegador.find_element(By.XPATH, '/html/body').get_attribute('innerHTML')

    # navegador.close()
    navegador.quit()
    
    return conteudo


def salvarArquivo(conteudo, nome):
    with open(nome,'w',encoding='UTF-8') as arquivo:
        arquivo.write(conteudo)


#salvarArquivo(obterConteudo('https://steamdb.info/charts/'),'charts')

def lerArquivo(nome):
    with open(nome,'r',encoding='UTF-8') as arquivo:
        conteudo= arquivo.read()

    return conteudo



    