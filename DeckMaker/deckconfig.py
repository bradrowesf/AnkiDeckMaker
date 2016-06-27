import json

class Configuration(object):

	def __init__(self, pathToConfig):
		# Load the configs
		configFile = open(pathToConfig)
		configRaw = configFile.read()
		self.configs = json.loads(configRaw)
		configFile.close()
			
	def getTestValue(self):
		return self.configs['testvalue']