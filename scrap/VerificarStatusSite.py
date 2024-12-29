class VerificarStatusSite:
	def __init__(self, url):
			self.url = url

	def verificar_status(self):
		try:
			response = requests.get(self.url)
			return response.status_code
		except Exception as e:
				return e