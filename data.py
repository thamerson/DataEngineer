import csv
from bs4 import BeautifulSoup

def lerArquivo(nome):
    with open(nome, 'r', encoding='UTF-8') as arquivo:
        conteudo = arquivo.read()

    return conteudo

conteudo_arquivo = lerArquivo('tabelas.html')

coleta = BeautifulSoup(conteudo_arquivo, 'html.parser')
tabelas = coleta.find_all('table', attrs={'class': 'table-products table-hover text-left dataTable'})

dados_tabela = []  
for tabela in tabelas:
    linhas = tabela.find_all('tr')

    
    cabecalhos = linhas[0].find_all('th')
    colunas = [cabecalho.get_text().strip() for cabecalho in cabecalhos]

    
    colunas = colunas[:1] + colunas[2:6]

   
    for linha in linhas[1:]:
        dados_linha = {}  
        
        colunas_linha = linha.find_all('td')

        valores_colunas = [coluna.get_text().strip() for i, coluna in enumerate(colunas_linha) if i != 1 and i != 6]

        for i, valor_coluna in enumerate(valores_colunas):
            dados_linha[colunas[i]] = valor_coluna

       
        dados_tabela.append(dados_linha)

DadosCsv = 'dados_tabela.csv'

with open(DadosCsv, 'w', newline='', encoding='UTF-8') as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    writer.writeheader()
    writer.writerows(dados_tabela)

print(f"Dados da tabela salvos no arquivo: {DadosCsv}")
