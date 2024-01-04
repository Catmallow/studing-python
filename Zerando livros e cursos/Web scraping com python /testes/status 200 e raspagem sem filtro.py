'''
descrição breve do codigo, é algo que pega tabelas por scraping e com base nisso faz um leve tratamento destes
dados para assim serem exibidos de uma forma mais crua por assim dizer

'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Especifica o URL que você deseja analisar
url = 'https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

# Faz uma solicitação HTTP para obter o conteúdo da página
response = requests.get(url)

"""
Verifica se a solicitação foi bem-sucedida (código de status 200)
Link do status 200:
https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/200
"""

if response.status_code == 200:
    # Obtém o conteúdo HTML da página
    html_content = response.text
    print('a requisição foi bem sucedida')

    # Cria um objeto BeautifulSoup usando o HTML obtido
    soup = BeautifulSoup(html_content, 'html.parser')
    dados1 = soup.find_all('th')
    dados2 = soup.find_all('td')
    print('Dados não tratados:', dados1)
    print('Dados não tratados:', dados2)


else:
    print(f"A solicitação falhou com o código de status {response.status_code}")

# convertendo os tipos de dados
dados1 = str(dados1)
dados2 = str(dados2)

# tratamento de dadados para a lista 1
cont_inter2 = dados1.replace('<th>','')
# print(cont_inter2)
novo_cont_inter2 = cont_inter2.replace('</th>','')
# print(novo_cont_inter2)

# tratamento de dados para lista 2
cont_inter3 = dados2.replace('<td>','')
# print(cont_inter3)
novo_cont_inter3 = cont_inter3.replace('</td>','')
print('dados tratados: ',novo_cont_inter3)

print('dados tratadso: ', novo_cont_inter2,novo_cont_inter3)

# ultimo passo pegar estes vetores para assim nomear as posições que estes ocupam e assim
# transformalos em matrizes x*2

# Exemplo de valores

# Criar uma lista com os valores
