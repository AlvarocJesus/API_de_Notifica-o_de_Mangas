class Database:
	def __init__(self):
		print('Database')

	def addManga(self, manga):
		print('Add manga')
		print(f'Data Manga: {manga}')

		engine = self.getEngine()

		with engine.connect() as conn:
			print('Connection')

	def getManga(self):
		print('Get manga')
		engine = self.getEngine()

		with engine.connect() as conn:
			print('Connection')
	
	def getEngine(self):
		print('Get engine')
