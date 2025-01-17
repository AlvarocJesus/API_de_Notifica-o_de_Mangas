import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bs4
import json
import requests
from unidecode import unidecode
from config.log.log import Log

class MangaBr:
	logger = None
	url = 'https://mangabr.net/manga/ao-ashi'

	def __init__(self):
		self.logger = Log().initLog('mangaBr.log')
	
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
			titulo = soup.find('title').text.strip().split(' - ')[0]
			# soup.find('h1', class_='mb-0 d-inline-block h2').text.strip()
			print(f'Titulo: {titulo}')
			ultimo_capitulo = ' '.join(soup.find('div', class_='col-12 chapters-list').find_all('div')[0].find('a').find('h5').text.strip().replace(' ', '').split('\n')[:2])
			print(f'Ultimo capitulo: {ultimo_capitulo}')
			url_ultimo_capitulo = soup.find('div', class_='col-12 chapters-list').find_all('div')[0].find('a')['href']
			print(f'Url ultimo capitulo: {url_ultimo_capitulo}')
			print(f'https://mangabr.net{url_ultimo_capitulo}')
			
			# data_ultimo_capitulo = soup.find('div', class_='col-12 chapters-list').find_all('div')[0].find('a').find('h5').text.strip().replace(' ', '').split('\n')[-1]
			# print(f'Data ultimo capitulo: {data_ultimo_capitulo}')

			Log().log(self.logger, 'info', 'Data extracted successfully')
			return { 
				'titulo': titulo,
				'ultimo_capitulo': ultimo_capitulo,
				'url_ultimo_capitulo': f'https://mangabr.net{url_ultimo_capitulo}'
			}
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')
	
	def format_data(self, data):
		print('Format data')
		print(json.dumps(data, indent=2))

	def run(self):
		soup = self.get_data(self.url)
		data = self.extract_data(soup)
		self.format_data(data)

if __name__ == '__main__':
	MangaBr().run()