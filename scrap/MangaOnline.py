import os
import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bs4
import json
import requests
from unidecode import unidecode
from config.log.log import Log

class MangaOnline:
	logger = None
	url = 'https://mangaonline.blog/manga/solo-leveling-ragnarok/'

	def __init__(self):
		self.logger = Log().initLog('mangaOnline_blog.log')

	def get_data(self, url):
		try:
			html = requests.get(url)
			soup = bs4.BeautifulSoup(html.text, 'html.parser')

			with open('teste.html', 'w', encoding='utf-8') as file:
				file.write(soup.prettify())

			Log().log(self.logger, 'info', 'Data retrieved successfully')
			return soup
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')
	
	def extract_data(self, soup):
		try:
			titulo = soup.find('div', class_='post-title').find('h1').text.strip()
			capitulo_recente = soup.find('div', class_='main version-chap no-volumn active').find_all('li')[0].find('a').text.strip().split(' ')[-1]
			ultimo_capitulo_link = soup.find('ul', class_='main version-chap no-volumn active').find_all('li')[0].find('a')['href']

			print(f'Titulo: {titulo}')
			# print(f'Capitulo: {capitulo_recente}')
			# print(f'Link: {ultimo_capitulo_link}')

			Log().log(self.logger, 'info', 'Data extracted successfully')
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')

	def format_data(self):
		pass

	def run(self):
		soup = self.get_data(self.url)
		self.extract_data(soup)

if __name__ == '__main__':
	MangaOnline().run()