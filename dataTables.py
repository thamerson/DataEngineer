import csv
from bs4 import BeautifulSoup

def lerArquivo(nome):
    with open(nome, 'r', encoding='UTF-8') as arquivo:
        conteudo = arquivo.read()

    return conteudo

conteudo_arquivo = lerArquivo('tabela0.html')

coleta = BeautifulSoup(conteudo_arquivo, 'html.parser')
tabelas = coleta.find_all('table', attrs={'class': 'table-sales table-hover dataTable no-footer'})

dados_tabela = []
for tabela in tabelas:
    linhas = tabela.find_all('tr')

    cabecalhos = linhas[0].find_all('th')

    colunas_validas = [i for i, th in enumerate(cabecalhos) if th.get_text().strip()]

    for linha in linhas[1:]:
        dados_linha = {}

        colunas_linha = linha.find_all('td')

        for indice, coluna in enumerate(colunas_linha):
            if indice in colunas_validas:
                conteudo_coluna = coluna.get_text().strip()
                if conteudo_coluna:
                    dados_linha[cabecalhos[indice].get_text().strip()] = conteudo_coluna

        dados_tabela.append(dados_linha)

DadosCsv = 'dados_tabela.csv'

cabecalhos_validos = [cabecalhos[indice].get_text().strip() for indice in colunas_validas]

with open(DadosCsv, 'w', newline='', encoding='UTF-8') as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos_validos)
    writer.writeheader()
    writer.writerows(dados_tabela)

print(f"Dados da extração: {DadosCsv}")
