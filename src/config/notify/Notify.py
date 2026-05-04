import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Notify:
	my_chat_id = '1215366778'

	def __init__(self):
		pass
  
	def sendMessage(self, message: str):
		try:
			print(f"Enviando mensagem: {message}")
			data = {
			  'chat_id': self.my_chat_id,
			  'text': message
			}

			url = 'https://api.telegram.org/bot{}/sendMessage'.format(os.getenv('TELEGRAM_API_KEY'))

			req = requests.post(url, data=data)
			print(f"Resposta: {req.text}")
		except Exception as e:
			print(f"Erro ao enviar mensagem: {str(e)}")


if __name__ == '__main__':
	Notify().sendMessage('Hello World!')