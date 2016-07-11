from notetranslator import NoteTranslator

class MidiStringMaker(object):

	def __init__(self, translator):
	
		self.myTranslator = translator
		self.myKeyDown = str(90)
		self.myKeyUp = str(80)
		self.myVelocity = str(60)
		self.ticksPerBeat = 960
		
	def AppendNote(self, note, placement, duration):
		# note - pitch to add
		# placement - beats following last event
		# duration - beats note held
		
		keyDown =  self.KeyDown(note, placement)
		keyUp = self.KeyUp(note, duration)
		outString = keyDown + keyUp
		
		return outString
	
	def AppendChord(self, notes, placement, duration):
		# notes - arrau of pitches to add
		# placement - beats following last event
		# duration - beats note held

		chordDown = self.ChordDown( notes, placement)
		chordUp = self.ChordUp( notes, duration)
		outString = chordDown + chordUp
		
		return outString
	
	def KeyDown(self, note, placement):
		# note - pitch to add
		# placement - beats following last event

		outString = "E "	# starts w/ this for some reason
		outString += str(int(self.ticksPerBeat*placement)) + " "	# 960 per beat
		outString += self.myKeyDown + " "	# note down
		outString += self.myTranslator.GetHexString(note) + " "
		outString += self.myVelocity # velocity
		outString += '\n' 
		
		return outString
		
	def KeyUp(self, note, placement):
		# note - pitch to add
		# placement - beats following last event
		
		outString = "E "	# starts w/ this for some reason
		outString += str(int(self.ticksPerBeat*placement)) + " "	# 960 per beat
		outString += self.myKeyUp + " "	# note up
		outString += self.myTranslator.GetHexString(note) + " "
		outString += self.myVelocity  # velocity
		outString += '\n'
		
		return outString
		
	def ChordDown(self, notes, placement):
		# a string for each note in notes
		
		outString = ""
		for note in notes:
			duration = 0
			if note == notes[0]:
				duration = placement
			outString += self.KeyDown( note, duration)
			
		return outString
		
	def ChordUp(self, notes, placement):
		# a string for each note in notes
		
		outString = ""
		for note in notes:
			duration = 0
			if note == notes[0]:
				duration = placement	# first note only
			outString += self.KeyUp( note, duration)
			
		return outString
	
	def TerminateString(self, placement = 0):
	
		outString = "E "
		outString += str( int(placement*self.ticksPerBeat))
		outString += " b0 7b 00\n"
		return outString
		
#test code
if __name__ == "__main__":
	t = NoteTranslator()
	sm = MidiStringMaker(t)
	
	humanNotes = ["Cb5","C#2","G7"]
	notes = []
	for note in humanNotes:
		notes.append(t.GetMidiCodeForHumans(note))
	
	print sm.AppendChord( notes, 3.5, 2)
