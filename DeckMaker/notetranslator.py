
from note import Note

class NoteTranslator(object):

	def __init__(self):
	
		self.noteTable = []
		possibleNotes = [ 'C','D','E','F','G','A','B' ]
		self.currentOctave = 0
		self.currentNote = 5 	# start on 'A'
		midiPitchValue = 21		# Lowest note on piano
		
		while midiPitchValue < 109: #change to 109 later
			if self.AccidentalCase(midiPitchValue) == 0:	# standard natural note
				noteName = possibleNotes[self.currentNote] + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				midiPitchValue += 1
			elif self.AccidentalCase(midiPitchValue) == 1:	# standard sharp/flat pair
				# add sharp
				noteName = possibleNotes[self.currentNote] + '#' + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				# move note, add flat, then move on
				self.IncrementNoteIndex()
				noteName = possibleNotes[self.currentNote] + 'b' + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				midiPitchValue += 1
			elif self.AccidentalCase(midiPitchValue) == 2:	# natural/flat pair
				# add natural
				noteName = possibleNotes[self.currentNote] + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				# move note, add flat, move note back, then move on
				self.IncrementNoteIndex()
				noteName = possibleNotes[self.currentNote] + 'b' + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				self.DecrementNoteIndex()
				midiPitchValue += 1
			else:	# sharp/natural pair
				# add sharp
				noteName = possibleNotes[self.currentNote] + '#' + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				# move note, add natural, move on
				self.IncrementNoteIndex()
				noteName = possibleNotes[self.currentNote] + str(self.currentOctave)
				self.noteTable.append( Note( noteName, midiPitchValue))
				midiPitchValue += 1
					
	def DumpNotes(self):
		
		# for debugging
		for note in self.noteTable:
			print note.Name() + " " + str(note.MidiValue()) + " " + str(note.ScaleValue())
		
	def GetMidiCode(self, inNote):
	
		# inNote is the human readable note name string
		for note in self.noteTable:
			if note.Name() == inNote:
				return note.MidiValue()
				
		# it's bad if you hit this		
		assert()
		
	def GetMidiCodeHexString(self, note):
	
		#return just the raw hex, no '0x' stuff
		outString = hex(self.GetMidiCode(note)).lstrip('0x')
		return outString
		
	def GetTriadCodes(self, lowestNote, quality, inversion):
	
		# inversion is 1 based like in music
		# lowest note (i.e. not necessarily the root of the chord)
		
		outNotes = []
		lowestNoteCode = self.GetMidiCode(lowestNote)
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
		
	def GetTriadHexCodeStrings(self, lowestNote, quality, inversion):
	
		outNoteStrings = []
		outNotes = self.GetTriadCodes( lowestNote, quality, inversion)
		for noteValue in outNotes:
			outNoteStrings.append( hex(noteValue).lstrip('0x'))
			
		return outNoteStrings
		
		
	def AccidentalCase(self, pitchValue):
	
		foo = ( pitchValue - 21 ) % 12
		
		if foo == 0 or foo == 5 or foo == 10:
			return 0
		elif foo == 1 or foo == 4 or foo == 6 or foo == 9 or foo == 11:
			return 1
		elif foo == 2 or foo == 7:
			return 2
		else:
			return 3
			
	def IncrementNoteIndex(self):
	
		if self.currentNote < 6:
			self.currentNote += 1
		else:
			self.currentNote = 0
			self.currentOctave += 1	# next octave

	def DecrementNoteIndex(self):
	
		if self.currentNote > 0:
			self.currentNote -= 1
		else:
			self.currentNote = 6
			self.currentOctave -= 1	# last octave
		
		
if __name__ == "__main__":

	translator = NoteTranslator()
	values = translator.GetTriadCodes( "C4", "minor", 3)
	print values
	values = translator.GetTriadCodes( "Ab2", "major", 2)
	print values
	values = translator.GetTriadCodes( "G#6", "minor", 1)
	print values
	
	valueStrings = translator.GetTriadHexCodeStrings( "C4", "major", 1)
	print valueStrings	
	valueStrings = translator.GetTriadHexCodeStrings( "Ab2", "major", 2)
	print valueStrings	
	valueStrings = translator.GetTriadHexCodeStrings( "G#6", "minor", 1)
	print valueStrings