import bs4
import json
import requests
from unidecode import unidecode
from config.log.log import Log

class MangaBr:
	def __init__(self):
		Log().initLog('mangaBr.log')
	
	def get_data(self, url):
		try:
			Log().log('info', 'Data retrieved successfully')
			return None
		except Exception as e:
			Log().log('error', f'Error: {e}')
	
	def extract_data(self):
		try:
			Log().log('info', 'Data extracted successfully')
			return None
		except Exception as e:
			Log().log('error', f'Error: {e}')
	
	def format_data(self):
		pass

	def run(self):
		pass