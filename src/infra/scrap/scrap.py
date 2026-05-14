import requests
from requests.adapters import HTTPAdapter, Retry
import bs4

from config.log.log import Log
from infra.db.database import Database

class Scrap():
	logger = None

	def __init__(self, url):
		print('Scrap')
		self.database = Database(database=False)
		self.logger = Log().initLog('scrap.log')
		self.session = requests.Session()
		retries = Retry(total=10, backoff_factor=1, status_forcelist=[502, 503, 504])
		self.session.mount('http://', HTTPAdapter(max_retries=retries))
		self.session.mount('https://', HTTPAdapter(max_retries=retries))
		
		self.url = url

	def get_data(self):
		try:
			""" headers = {
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

			html = requests.get(self.url, headers=headers)"""

			html = self.session.get(self.url)
			
			if html.status_code != 200:
				self.database.deactivateMangaSite(self.url)
				Log().log(self.logger, 'error', f'Error: {html.status_code}')
				return None

			soup = bs4.BeautifulSoup(html.text, 'html.parser')
			Log().log(self.logger, 'info', 'Data retrieved successfully')
			return soup
		except Exception as e:
			print('Exception occurred') # Log para depuração
			Log().log(self.logger, 'error', f'Error: {e}')

	def verificar_status(self):
		try:
			response = requests.get(self.url)
			return response.status_code
		except Exception as e:
			return e