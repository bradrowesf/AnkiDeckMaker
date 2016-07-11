
class Note(object):

	def __init__(self, midivalue):
	
		if midivalue < 12 or midivalue > 108:
			print midivalue
			assert()	#sanity checking
			
		self.myNames = []
		self.myMidiValue = midivalue	# midicode (base 10)
		self.myScaleValue = midivalue - 12	# distance from C1

		#name thyself
		octaveVal = (self.myScaleValue // 12) + 1
		octave = str(octaveVal)
		
		scaleDegree = self.myScaleValue % 12
		
		if scaleDegree == 0:
			self.myNames.append( 'B#' + str(octaveVal -1)) # in last octave actually
			self.myNames.append( 'C' + octave)
		elif scaleDegree == 1:
			self.myNames.append( 'C#' + octave)
			self.myNames.append( 'Db' + octave)
		elif scaleDegree == 2:
			self.myNames.append( 'D' + octave)
		elif scaleDegree == 3:
			self.myNames.append( 'D#' + octave)
			self.myNames.append( 'Eb' + octave)
		elif scaleDegree == 4:
			self.myNames.append( 'E' + octave)
			self.myNames.append( 'Fb' + octave)
		elif scaleDegree == 5:
			self.myNames.append( 'E#' + octave)
			self.myNames.append( 'F' + octave)
		elif scaleDegree == 6:
			self.myNames.append( 'F#' + octave)
			self.myNames.append( 'Gb' + octave)
		elif scaleDegree == 7:
			self.myNames.append( 'G' + octave)
		elif scaleDegree == 8:
			self.myNames.append( 'G#' + octave)
			self.myNames.append( 'Ab' + octave) 
		elif scaleDegree == 9:
			self.myNames.append( 'A' + octave)
		elif scaleDegree == 10:
			self.myNames.append( 'A#' + octave)
			self.myNames.append( 'Bb' + octave)
		elif scaleDegree == 11:
			self.myNames.append( 'B' + octave)
			self.myNames.append( 'Cb' + str(octaveVal +1)) # in next octave actually
		else:
			assert()	#bad
		
	def Names(self):
		
		return self.myNames
		
	def MidiValue(self):
	
		return self.myMidiValue
		
	def ScaleValue(self):
	
		return self.myScaleValue


#test code
if __name__ == "__main__":
	note = Note(57)
	print note.Names()
	print note.MidiValue()
	print note.ScaleValue()