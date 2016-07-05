from notetranslator import NoteTranslator

class MidiStringMaker(object):

	def __init__(self, translator):
	
		self.myTranslator = translator
		self.myKeyDown = str(90)
		self.myKeyUp = str(80)
		self.myVelocity = str(60)
		self.ticksPerBeat = 960
		
	def AppendNote(self, note, placement, duration):
		
		keyDown =  self.KeyDown(note, placement, duration, True)
		keyUp = self.KeyUp(note, placement, duration, False)
		outString = keyDown + keyUp
		
		return outString
		
	def KeyDown(self, note, placement, duration, newline):
		# note - pitch to add
		# placement - beats following last event
		# duration - beats note held

		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*placement) + " "	# 960 per beat
		outString += self.myKeyDown + " "	# note down
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += self.myVelocity # velocity
		if newline==True:
			outString += '\n' 
		
		return outString
		
	def KeyUp(self, note, placement, duration, newline):
		# note - pitch to add
		# placement - beats following last event
		# duration - beats note held
		
		outString = "E "	# starts w/ this for some reason
		outString += str(self.ticksPerBeat*duration) + " "	# 960 per beat
		outString += self.myKeyUp + " "	# note down
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += self.myVelocity + '\n' # velocity
		if newline==True:
			outString += '\n'
		
		return outString
		
		
if __name__ == "__main__":
	translator = NoteTranslator()
	stringMaker = MidiStringMaker(translator)
	print stringMaker.AppendNote( "E5", 3, 1)