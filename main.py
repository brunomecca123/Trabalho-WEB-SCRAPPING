from bs4 import BeautifulSoup
import requests
import html5lib

html = requests.get("https://www.estantevirtual.com.br/estante/engenharia").text
soup = BeautifulSoup(html, 'html5lib')

todosnomes = soup.find_all('h2')
todosautores = soup.find_all('span', {'itemprop': 'author'})
todosprecos = soup.find_all('span', {'class': 'preco'})

text = ''
conteudo = []

with open('livros.txt', 'w') as arquivo:
    for nome, autor, preco in zip(todosnomes, todosautores, todosprecos):
        conteudo.append('{} {} {} \n \n'.format(nome.text, autor.text, preco.text))

        arquivo.writelines(conteudo)
        arquivo.close

