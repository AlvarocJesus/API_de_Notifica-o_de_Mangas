import os
import requests

class Notify:
	def __init__(self):
		pass
  
	async def sendMessage(self, token: str, message: str, chat_id: str = os.getenv('TELEGRAM_API_KEY')):
		try:
			data = {
			  'chat_id': chat_id,
			  'text': message
			}

			url = 'https://api.telegram.org/bot{}/sendMessage'.format(token)

			await requests.post(url, data=data)
		except Exception as e:
			print(f"Erro ao enviar mensagem: {str(e)}")