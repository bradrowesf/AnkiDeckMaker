
class NoteTranslator(object):

	def __init__(self):
	
		self.noteTable = {}
		possibleNotes = [ 'A','B','C','D','E','F','G' ]
		currentOctave = 0
		currentNote = 0
		midiPitchValue = 21
		while midiPitchValue < 33: #change to 109 later
			print midiPitchValue
			self.noteTable[ possibleNotes[currentNote] + str(currentOctave) ] = midiPitchValue 
			midiPitchValue += 1
			
			if self.HasSharp( possibleNotes[currentNote] ):
				self.noteTable[ possibleNotes[currentNote] + '#' + str(currentOctave) ] = midiPitchValue
				
			if currentNote < len(possibleNotes) - 1:
				currentNote += 1
			else:
				currentNote = 0

##			if possibleNote[currentNote] != 'B' and possibleNote[currentNote] != 'E':
##			self.noteTable.append( possibleNote[currentNote] + '#' + str(currentOctave), midiPitchValue )
##			self.noteTable.append( possibleNote[currentNote + 1]  + 'b' + str(currentOctave), midiPitchValue )
				
	def DumpTable(self):
		
		print self.noteTable
		
	def HasSharp(self, note):
	
		#Add Sharp for A, C, D, F, G
		if note == 'A' or note == 'C' or note == 'D' or note == 'F' or note == 'G':
			return True
			
		return False