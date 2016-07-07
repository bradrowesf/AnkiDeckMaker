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
		
		keyDown =  self.KeyDown(note, placement, True)
		keyUp = self.KeyUp(note, duration, False)
		outString = keyDown + keyUp
		
		return outString
		
	def KeyDown(self, note, placement, newline):
		# note - pitch to add
		# placement - beats following last event

		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*placement) + " "	# 960 per beat
		outString += self.myKeyDown + " "	# note down
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += self.myVelocity # velocity
		if newline==True:
			outString += '\n' 
		
		return outString
		
	def KeyUp(self, note, placement, newline):
		# note - pitch to add
		# placement - beats following last event
		
		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*placement) + " "	# 960 per beat
		outString += self.myKeyUp + " "	# note up
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += self.myVelocity + '\n' # velocity
		if newline==True:
			outString += '\n'
		
		return outString
		
#test code
if __name__ == "__main__":
	translator = NoteTranslator()
	stringMaker = MidiStringMaker(translator)
	print stringMaker.AppendNote( "A#2", 3, 7)