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
	# url = 'https://mangaonline.blog/manga/solo-leveling-ragnarok/'
	# url_chapters = 'https://mangaonline.blog/manga/solo-leveling-ragnarok/ajax/chapters/'

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
	
	def get_data_chapters(self, url_chapters):
		try:
			headers = {
				'accept': '*/*',
				'accept-language': 'pt-BR,pt;q=0.7',
				'content-length': '0',
				'cookie': 'wpmanga-reading-history=W3siaWQiOjE5NjcsImMiOiI0NzY3IiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQyODV9LHsiaWQiOjE4NjAsImMiOiI0NzY4IiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQyODR9LHsiaWQiOjE4NjQsImMiOiI0ODAxIiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQzMjF9LHsiaWQiOjIwNzAsImMiOiI0Nzg1IiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQyODZ9LHsiaWQiOjE5NTUsImMiOiI0Nzc1IiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQyODZ9LHsiaWQiOjE5NjUsImMiOiI0NzcwIiwicCI6MSwiaSI6IiIsInQiOjE3MzY4NTQyODd9LHsiaWQiOjI1MjYsImMiOiI0Nzc0IiwicCI6MSwiaSI6IinQiOjE3MzY4NTQyODd9XQ%3D%3D',
				'origin': 'https://mangaonline.blog',
				'priority': 'u=1, i',
				'referer': 'https://mangaonline.blog/manga/solo-leveling-ragnarok/',
				'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'sec-gpc': '1',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
				'x-requested-with': 'XMLHttpRequest'
			}

			html = requests.post(url_chapters)
			soup = bs4.BeautifulSoup(html.text, 'html.parser')

			with open('teste_chapters.html', 'w', encoding='utf-8') as file:
				file.write(soup.prettify())

			Log().log(self.logger, 'info', 'Data retrieved successfully')
			return soup
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')
	
	def extract_data(self, soup, soup_chapters):
		try:
			titulo = soup.find('div', class_='post-title').find('h1').text.strip()
			# print(f'Titulo: {titulo}')
			 
			capitulo_recente = ' '.join(soup_chapters.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a').text.strip().split(' ')[:2])
			# print(f'Capitulo: {capitulo_recente}')
			
			ultimo_capitulo_link = soup_chapters.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find('a')['href']
			# print(f'Link: {ultimo_capitulo_link}')

			data_atualizacao = soup_chapters.find('ul', class_='main version-chap no-volumn').find_all('li')[0].find_all('a')[-1]['title']
			# print(f'Ultima atualiacao: {data_atualizacao}')

			Log().log(self.logger, 'info', 'Data extracted successfully')
			
			return {
				'titulo': titulo,
				'capitulo': capitulo_recente,
				'link': ultimo_capitulo_link,
				'data_atualizacao': data_atualizacao
			}
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')

	def format_data(self, data):
		print(json.dumps(data, indent=4))

	def run(self):
		soup = self.get_data(self.url)
		soup_chapters = self.get_data_chapters(self.url_chapters)
		data = self.extract_data(soup, soup_chapters)
		self.format_data(data)

if __name__ == '__main__':
	MangaOnline().run()