import argparse

class DeckOptions(object):
	
	def __init__(self):
		
		parser = argparse.ArgumentParser()
		self.addArgs(parser)
		self.args = parser.parse_args()
		
	def addArgs(self, parser):
	
		parser.add_argument("pathToConfig", type=str,
							help="Path to config file")
		parser.add_argument("pathToOutput", type=str,
							help="Path to output file")
		
	def pathToConfig(self):
		return self.args.pathToConfig
		
	def pathToOutput(self):
		return self.args.pathToOutput