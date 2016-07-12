import argparse

from deckoptions import DeckOptions
from deckconfig import Configuration
from notetranslator import NoteTranslator
from filemanager import FileManager
from midistringmaker import MidiStringMaker
from miditrackmaker import MidiTrackMaker

#fileManager = FileManager(options.pathToOutput())
#fileManager.Write()

class Card(object):

	def __init__(self, cadence, quality, note, name):
	
		self.Cadence = cadence
		self.Quality = quality
		self.Note = note
		self.Name = name
		

class DeckMaker(object):

	def __init__(self):
	
		options = DeckOptions()
		self.myConfig = Configuration(options.pathToConfig())
		self.t = NoteTranslator()
		self.sm = MidiStringMaker(self.t)
		self.tm = MidiTrackMaker(self.t,self.sm)
		
	def Run(self):
	
		if self.myConfig.getProgram() == "Cadence-One Note":
			self.CadenceOneNote()
		else:
			assert()	#bad
			
	def CadenceOneNote(self):
	
		#Build Card Array
		cards = []
		cadenceRoot = "C4"
		notes = ["C5","G5","E5","D5","F5","A5","B5","Eb5","Ab5","Bb5","Db5","Gb5"]
		names = ["Do","Sol","Mi","Re","Fa","La","Ti","Ri/Me","Si/Le","Li/Te","Di/Ra","Fi/Se"]
		
		#once major
		for i in range(len(notes)):
			cards.append(Card(self.t.GetMidiCodeForHumans("C4"), "major", self.t.GetMidiCodeForHumans(notes[i]), names[i]))
			
		#once minor
		for i in range(len(notes)):
			cards.append(Card(self.t.GetMidiCodeForHumans("C4"), "major", self.t.GetMidiCodeForHumans(notes[i]), names[i]))
	
		#build the tracks
		for card in cards:
			self.tm.OpenRegion(card.Name)
			self.tm.AppendCadence( card.Cadence, card.Quality)
			self.tm.AppendOneNote( card.Note)
			self.tm.CloseRegion()
			
		self.tm.Terminate()
	

if __name__ == "__main__":

	app = DeckMaker()
	app.Run()