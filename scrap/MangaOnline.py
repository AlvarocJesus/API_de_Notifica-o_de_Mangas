from config.log.log import Log

class MangaOnline:
	def __init__(self):
		Log().initLog('mangaOnline.log')

	def get_data(self):
		try:
			Log().log('info', 'Data retrieved successfully')
			return None
		except Exception as e:
			Log().log('error', f'Error: {e}')
	
	def extract_data(self):
		try:
			Log().log('info', 'Data extracted successfully')
		except Exception as e:
			Log().log('error', f'Error: {e}')

	def format_data(self):
		pass

	def run(self):
		pass