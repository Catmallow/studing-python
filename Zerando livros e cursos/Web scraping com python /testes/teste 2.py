# configurando o ambiente
import requests
from bs4 import BeautifulSoup

# Especifica o URL que você deseja analisar
url = 'https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

# Faz uma solicitação HTTP para obter o conteúdo da página
# Dicas revisar um pouco de redes e como a obtenção de dados funciona
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida (código de status 200)






if response.status_code == 200:
    # Obtém o conteúdo HTML da página
    html_content = response.text

    print('A solicitação ocorreu com sucesso')

    # Cria um objeto BeautifulSoup usando o HTML obtido
    soup = BeautifulSoup(html_content, 'html.parser')

    nova_lista_1 = soup.find_all('th')
    # nova_lista_2 = [soup.find_all('td')]

    print(nova_lista_1 )




    # print(response.text)



else:
    print(f"A solicitação falhou com o código de status {response.status_code}")

print(nova_lista_1)