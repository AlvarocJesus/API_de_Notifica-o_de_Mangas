import logging

class Log:
	encoding = ''
	level = ''
	logFormat = ''
	datefmt = ''
	
	def __init__(self):
		print('Log')
		self.encoding = 'utf-8'
		self.level = logging.DEBUG
		self.logFormat = '%(asctime)s | %(levelname)s | %(message)s'
		self.datefmt='%m/%d/%Y %I:%M:%S %p'
	
	def initLog(self, fileName):
		print('initLog')
		logger = logging.getLogger(__name__)
		logging.basicConfig(filename=fileName, encoding = self.encoding, level = self.level, format=self.logFormat, datefmt=self.datefmt)

		return logger
	
	def log(self, logger, level, msg):
		print('log')
		match level:
			case 'debug':
				print('debug')
				logger.debug(msg)
			case 'info':
				print('info')
				logger.info(msg)
			case 'warning':
				print('warning')
				logger.warning(msg)
			case 'error':
				print('error')
				logger.error(msg)
			case 'critical':
				print('critical')
				logger.critical(msg)
