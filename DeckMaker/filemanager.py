from deckconfig import Configuration
from miditrackmaker import MidiTrackMaker


class FileManager(object):

	def __init__(self, config, trackmaker):
	
		self.myConfig = config
		self.myTM = trackmaker
		
	def WriteMidiFile(self):
	
		file = open(self.myConfig.getMidiOutputFile(), 'w')
		file.write(self.myTM.Track())
		file.write(str(self.myTM.Length()))
		file.close()
		
	def WriteRegionFile(self):
	
		file = open(self.myConfig.getRegionOutputFile(), 'w')
		file.write(self.myTM.Regions())
		file.close()

	def TestWrite(self):
	
		file = open(self.myConfig.getMidiOutputFile(), 'w')
		file.write("Tester Midi Output")
		file.close()
		file = open(self.myConfig.getRegionOutputFile(), 'w')
		file.write("Test Region Output")
		file.close()
