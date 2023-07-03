# Bem-vindo ao Repositório de Resolução do Case Técnico

Este repositório contém a minha solução para o caso técnico solicitado. A solução foi dividida em vários arquivos, cada um responsável por uma etapa específica do processo.

Se tiver dúvidas, sinta-se à vontade para abrir um issue aqui no GitHub ou entrar em contato por e-mail.

## Instruções de Uso

O processo para utilizar os scripts deste repositório envolve três etapas principais, descritas abaixo:

### 1. Extração do HTML Completo

Execute o arquivo `extractFullHTML.py` com a URL desejada. Isso irá coletar e salvar todo o HTML da URL em um arquivo no seu diretório local.


<python extractFullHTML.py>

 
### 2. Extração de Tabelas

Agora, execute o arquivo `extractTables.py`. Este código lê o arquivo HTML baixado na etapa anterior e extrai todas as tabelas encontradas, salvando-as em outro arquivo HTML no diretório local.


<python extractTables.py>


### 3. Criação de Arquivos CSV

Por fim, execute o código `dataTables.py`. Este script lê o arquivo HTML das tabelas gerado na etapa anterior, extrai as linhas e colunas das tabelas e salva esses dados em um arquivo CSV.

<python dataTables.py>




