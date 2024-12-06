import bs4
import json
import requests
from unidecode import unidecode

class OldiSussy:
	def __init__(self):
		print('OldiSussy')

	url = 'https://oldi.sussytoons.com/manga/logando-10-000-anos-no-futuro/'

	"""  url = 'https://www.amazon.com.br/Monitor-Gamer-AOC-FreeSync-Q27G2/dp/B0C6FHZW5C'
	preço amazon
	print(soup.title)
	print(soup.find('span', class_="a-price").find('span', class_="a-offscreen")) """

	def get_data(self, url):
		try:
			html = requests.get(url)
			soup = bs4.BeautifulSoup(html.text, 'html.parser')

			with open('teste.html', 'w', encoding='utf-8') as file:
				file.write(soup.prettify())
			
			return soup
		except Exception as e:
			print(f'Error: {e}')

	def extract_data(self, soup):
		try:
			titulo = soup.find('div', class_='post-title').find('h1').text.strip()
			capitulo_mais_novo = soup.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a').text.strip()
			ultimo_capitulo_link = soup.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a')['href']

			print(f'Titulo: {titulo}')			
			print(f'Capitulo: {capitulo_mais_novo}')
			print(f'Link: {ultimo_capitulo_link}')

			return { 'titulo': titulo, 'capitulo_mais_novo': unidecode(capitulo_mais_novo), 'ultimo_capitulo_link': ultimo_capitulo_link }
		except Exception as e:
			print(f'Error: {e}')
	
	def format_data(self, data):
		print(f'Data: {json.dumps(data, indent=2)}')

	def run(self):
		soup = self.get_data(self.url)
		data = self.extract_data(soup)
		self.format_data(data)

OldiSussy().run()