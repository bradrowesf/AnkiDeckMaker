
class Note(object):

	def __init__(self, name, midivalue):
	
		self.myName = name				# readable value
		self.myMidiValue = midivalue	# midicode (base 10)
		self.myScaleValue = midivalue - 21	# distance from lowest piano note
		
	def Name(self):
		
		return self.myName
		
	def MidiValue(self):
	
		return self.myMidiValue
		
	def ScaleValue(self):
	
		return self.myScaleValue
