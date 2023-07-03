import time
import random
from undetected_chromedriver import Chrome, ChromeOptions

def obterConteudo(url):
    options = ChromeOptions()
    options.add_argument('--disable-web-security')

    with Chrome(options=options) as navegador:
        navegador.get(url)
        
        time.sleep(random.randint(500, 550))
        
        conteudo = navegador.page_source
        
    return conteudo

def main():
    conteudo = obterConteudo('https://steamdb.info/sales/')
    
    with open('pagina.html', 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

if __name__ == '__main__':
    main()
