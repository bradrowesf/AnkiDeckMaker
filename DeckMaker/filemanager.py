

class FileManager(object):

	def __init__(self, path):
	
		self.outputPath = path
		
	def Write(self, inData):
	
		file = open(self.outputPath, 'w')
		file.write(inData)
		file.close()