
from note import Note

class NoteTranslator(object):

	def __init__(self):
	
		self.noteTable = []
		midiPitchValue = 21				# Lowest note on piano
		while midiPitchValue <= 108:	# highest note on piano
			self.noteTable.append(Note(midiPitchValue))
			midiPitchValue += 1
					
	def DumpNotes(self):
		
		# for debugging
		for note in self.noteTable:
			print note.Names()
			print "MidiValue: " + str(note.MidiValue())
			print "ScaleValue: " + str(note.ScaleValue())
		
	def GetMidiCodeForHumans(self, inNote):
	
		# inNote is the human readable note name string
		
		for note in self.noteTable:
			if inNote in note.Names():
				return note.MidiValue()
				
		# it's bad if you hit this		
		assert()
		
	def GetHexString(self, note):
	
		#return just the raw hex, no '0x' stuff
		outString = hex(note).lstrip('0x')
		return outString
		
	def GetTriadCodes(self, lowestNoteCode, quality, inversion):
	
		# inversion is 1 based like in music
		# lowest note midi code (i.e. not necessarily the root of the chord)
		
		outNotes = []
		outNotes.append(lowestNoteCode)  # we know this ones there
		thirdSteps = 0	# changed later
		fifthSteps = 7
		octaveSteps = 12
		
		# major or minor third
		if quality == "major":
			thirdSteps = 4
		elif quality == "minor":
			thirdSteps = 3
		else:
			assert() #bad
		
		if inversion == 1:
			outNotes.append(lowestNoteCode + thirdSteps)
			outNotes.append(lowestNoteCode + fifthSteps)
		elif inversion == 2:
			outNotes.append(lowestNoteCode - thirdSteps + octaveSteps)
			outNotes.append(lowestNoteCode - thirdSteps + fifthSteps)
		elif inversion == 3:
			outNotes.append(lowestNoteCode - fifthSteps + octaveSteps)
			outNotes.append(lowestNoteCode - fifthSteps + octaveSteps + thirdSteps)
		else:
			assert() #bad
			
		return outNotes

	def GetTriadHexCodeStrings(self, lowestNoteCode, quality, inversion):
	
		outNoteStrings = []
		outNotes = self.GetTriadCodes( lowestNoteCode, quality, inversion)
		for noteValue in outNotes:
			outNoteStrings.append( self.GetHexString(noteValue))
			
		return outNoteStrings
		
if __name__ == "__main__":

	t = NoteTranslator()
	print "Translator Instantiated"

	values = t.GetTriadCodes( t.GetMidiCodeForHumans("C4"), "minor", 3)
	print values
	values = t.GetTriadCodes( t.GetMidiCodeForHumans("Ab2"), "major", 2)
	print values
	values = t.GetTriadCodes( t.GetMidiCodeForHumans("G#6"), "minor", 1)
	print values
	
	valueStrings = t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("C4"), "major", 1)
	print valueStrings	
	valueStrings = t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("Ab2"), "major", 2)
	print valueStrings	
	valueStrings = t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("G#6"), "minor", 1)
	print valueStrings