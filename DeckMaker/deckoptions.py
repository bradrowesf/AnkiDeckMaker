import argparse

class DeckOptions(object):
	
	def __init__(self):
		
		parser = argparse.ArgumentParser()
		self.addArgs(parser)
		self.args = parser.parse_args()
		
	def addArgs(self, parser):
	
		parser.add_argument("pathToConfig", type=str,
							help="Path to config file")
		
	def pathToConfig(self):
	
		return self.args.pathToConfig