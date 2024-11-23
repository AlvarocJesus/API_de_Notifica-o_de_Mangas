import requests
import bs4

# url = 'https://www.amazon.com.br/Monitor-Gamer-AOC-FreeSync-Q27G2/dp/B0C6FHZW5C'
url = 'https://oldi.sussytoons.com/manga/logando-10-000-anos-no-futuro/'

test = requests.get(url)
soup = bs4.BeautifulSoup(test.text, 'html.parser')

with open('teste.html', 'w', encoding='utf-8') as file:
	file.write(soup.prettify())

print(soup.title)
print(soup.find('div', class_='post-title').find('h1').text.strip())
capitulos = soup.find('ul', class_='main version-chap no-volumn').find_all('li')
ultimo_capitulo = soup.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a').text.strip()
ultimo_capitulo_link = soup.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a')['href']
# print(capitulos)
print(ultimo_capitulo)
# print(ultimo_capitulo_link)

for capitulo in capitulos:
	cap = capitulo.find('a')
	# print(f'Capitulo: {cap.text}')
	# print(f'Link: {cap["href"]}')

""" preço amazon
print(soup.title)
print(soup.find('span', class_="a-price").find('span', class_="a-offscreen")) """