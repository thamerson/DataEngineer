import csv
from bs4 import BeautifulSoup

def lerArquivo(nome):
    with open(nome, 'r', encoding='UTF-8') as arquivo:
        conteudo = arquivo.read()

    return conteudo

def salvarArquivo(conteudo, nome):
    with open(nome, 'w', encoding='UTF-8') as arquivo:
        arquivo.write(conteudo)

conteudo_arquivo = lerArquivo('pagina.html')

coleta = BeautifulSoup(conteudo_arquivo, 'html.parser')
tabelas = coleta.find_all('table', attrs={'class': 'table-sales table-hover dataTable no-footer'})

for tabela in tabelas:
    tabela_str = str(tabela)
    salvarArquivo(tabela_str, 'tabela{}.html'.format(tabelas.index(tabela)))
