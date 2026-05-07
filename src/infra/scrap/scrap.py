import requests
import bs4

from config.log.log import Log

class Scrap():
	logger = None

	def __init__(self):
		pass

	def get_data(self, url):
		try:
			headers = {
				'Accept': 'application/json, text/plain, */*',
				'Accept-Encoding': 'gzip, deflate, br, zstd',
				'Connection': 'keep-alive',
				'Host': 'api-dev.sussytoons.site',
				'Origin': 'https://www.sussytoons.site',
				'Referer': 'https://www.sussytoons.site/',
				'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-site',
				'Sec-GPC': '1',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
				'accept-language': 'pt-br,pt;q=0.9,en-us;q=0.8,en;q=0.7',
				'scan-id': '1',
				'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': "Windows"
			}
			
			html = requests.get(url, headers=headers)
			soup = bs4.BeautifulSoup(html.text, 'html.parser')

			# with open('teste.html', 'w', encoding='utf-8') as file:
			# 	file.write(soup.prettify())

			Log().log(self.logger, 'info', 'Data retrieved successfully')
			return soup
		except Exception as e:
			Log().log(self.logger, 'error', f'Error: {e}')

	def verificar_status(self):
		try:
			response = requests.get(self.url)
			return response.status_code
		except Exception as e:
			return e