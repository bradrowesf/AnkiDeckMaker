import argparse

class DeckOptions(object):
	
	def __init__(self, parser):
		
		parser.add_argument("pathToConfig")
		self.args = parser.parse_args()
		
	def pathToConfig(self):
	
		return self.args.pathToConfig