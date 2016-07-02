from notetranslator import NoteTranslator

class MidiStringMaker(object):

	def __init__(self, translator):
	
		self.myTranslator = translator
		
	def AppendNote(self, note, placement, duration):
		# note - pitch to add
		# placement - beats following last event
		# duration - beats note held
		
		#Build keydown
		outString = "E "	# starts w/ this for some reason
		outString += str(960*placement) + " "	# 960 per beat
		outString += str(90) + " "	# note down
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += str(60) + '\n' # velocity
		
		#Build keyup
		outString += "E "	# starts w/ this for some reason
		outString += str(960*duration) + " "	# 960 per beat
		outString += str(80) + " "	# note down
		outString += self.myTranslator.GetMidiNoteHexString(note) + " "
		outString += str(60) # velocity
		
		return outString
		
		
		
		
		
if __name__ == "__main__":
	translator = NoteTranslator()
	stringMaker = MidiStringMaker(translator)
	print stringMaker.AppendNote( "E5", 3, 1)