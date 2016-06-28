
class NoteTranslator(object):

	def __init__(self):
	
		self.noteTable = {}
		possibleNotes = [ 'C','D','E','F','G','A','B' ]
		self.currentOctave = 0
		self.currentNote = 5 	# start on 'A'
		midiPitchValue = 21		# Lowest note on piano
		
		while midiPitchValue < 109: #change to 109 later
			if self.AccidentalCase(midiPitchValue) == 0:	# standard natural note
				self.noteTable[ possibleNotes[self.currentNote] + str(self.currentOctave) ] = midiPitchValue 
				midiPitchValue += 1
			elif self.AccidentalCase(midiPitchValue) == 1:	# standard sharp/flat pair
				# add sharp
				self.noteTable[ possibleNotes[self.currentNote] + '#' + str(self.currentOctave) ] = midiPitchValue
				# move note, add flat, then move on
				self.IncrementNoteIndex()
				self.noteTable[ possibleNotes[self.currentNote] + 'b' + str(self.currentOctave) ] = midiPitchValue
				midiPitchValue += 1
			elif self.AccidentalCase(midiPitchValue) == 2:	# natural/flat pair
				# add natural
				self.noteTable[ possibleNotes[self.currentNote] + str(self.currentOctave) ] = midiPitchValue 
				# move note, add flat, move note back, then move on
				self.IncrementNoteIndex()
				self.noteTable[ possibleNotes[self.currentNote] + 'b' + str(self.currentOctave) ] = midiPitchValue
				self.DecrementNoteIndex()
				midiPitchValue += 1
			else:	# sharp/natural pair
				# add sharp
				self.noteTable[ possibleNotes[self.currentNote] + '#' + str(self.currentOctave) ] = midiPitchValue
				# move note, add natural, move on
				self.IncrementNoteIndex()
				self.noteTable[ possibleNotes[self.currentNote] + str(self.currentOctave) ] = midiPitchValue 
				midiPitchValue += 1
					
	def DumpTable(self):
		
		print self.noteTable
		
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
		