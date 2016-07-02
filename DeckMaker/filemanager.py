

class FileManager(object):

	def __init__(self, path):
	
		self.outputPath = path
		
	def Write(self):
	
		file = open(self.outputPath, 'w')
		file.write("E 3840 90 3f 60")
		file.close()