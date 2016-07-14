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
		self.fm = FileManager( self.myConfig, self.tm)
		
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
		names = ["Do","Sol","Mi","Re","Fa","La","Ti","Ri or Me","Si or Le","Li or Te","Di or Ra","Fi or Se"]
		
		#once major
		counter = 1
		for i in range(len(notes)):
			cards.append(Card(self.t.GetMidiCodeForHumans("C4"), "major", self.t.GetMidiCodeForHumans(notes[i]), "(" + str(counter) + ") " + names[i]))
			counter += 1
			
		#once minor
		for i in range(len(notes)):
			cards.append(Card(self.t.GetMidiCodeForHumans("C4"), "minor", self.t.GetMidiCodeForHumans(notes[i]), "(" + str(counter) + ") "  + names[i]))
			counter += 1
	
		#build the tracks
		for card in cards:
			self.tm.OpenRegion(card.Name)
			self.tm.AppendCadence( card.Cadence, card.Quality)
			self.tm.AppendOneNote( card.Note)
			self.tm.CloseRegion()
			
		self.tm.Terminate()
	
		# write out files
		self.fm.WriteMidiFile()
		self.fm.WriteRegionFile()
		
	def TestFileManager(self):
	
		self.fm.TestWrite()

if __name__ == "__main__":

	app = DeckMaker()
	app.Run()
	#app.TestFileManager()