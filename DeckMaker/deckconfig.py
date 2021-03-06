import json

class Configuration(object):

	def __init__(self, pathToConfig):
		# Load the configs
		configFile = open(pathToConfig)
		configRaw = configFile.read()
		self.configs = json.loads(configRaw)
		configFile.close()
			
	def getUpperRange(self):
		return self.configs['upper_range']
		
	def getLowerRange(self):
		return self.configs['lower_range']
		
	def getProgram(self):
		return self.configs['Program']
		
	def getMidiOutputFile(self):
		return self.configs['MidiOutputFile']
		
	def getRegionOutputFile(self):
		return self.configs['RegionOutputFile']