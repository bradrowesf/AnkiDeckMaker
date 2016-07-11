from notetranslator import NoteTranslator
from midistringmaker import MidiStringMaker

class MidiTrackMaker(object):

	def __init__(self, translator, stringmaker):
	
		self.myTrack = ""
		self.myT = translator
		self.mySM = stringmaker
		self.myLength = 0	#beats
		self.myBuffer = 0		
	
	def AppendCadence( self, key, quality):
	
		# key is in midicode
		# quality - major, minor
		
		tenthSteps = 0
		if quality == "major":
			tenthSteps = 16
		elif quality == "minor":
			tenthSteps = 15
		else:
			assert()
		
		# Build Notes for chords
		
		# (I or i)
		rootNotes = []
		rootNotes.append(key)	# for sure
		
		# upper inversion
		lowNote = key + tenthSteps
		rootNotes += self.myT.GetTriadCodes( lowNote, quality, 2)	# 2nd Inversion
			
		# (IV or iv)
		fourNotes = []
		root = key + 5	# up a perfect 4th
		fourNotes.append(root)
		
		# upper inversion
		lowNote = root + 12
		fourNotes += self.myT.GetTriadCodes( lowNote, quality, 1)	# 1st Inversion
		
		# (V or v)
		fiveNotes = []
		root = key + 7
		fiveNotes.append(root)
		
		# upper inversion
		lowNote = root + 7
		fiveNotes += self.myT.GetTriadCodes( lowNote, quality, 3)	# 3rd Inversion
		
		# build strings
		
		self.myTrack += self.mySM.AppendChord( rootNotes, self.myBuffer, 2)		# hold for 2 beats
		self.myTrack += self.mySM.AppendChord( fourNotes, 0, 1)		# 1 beat
		self.myTrack += self.mySM.AppendChord( fiveNotes, 0, 1)
		self.myTrack += self.mySM.AppendChord( rootNotes, 0, 4)		# 4 beats
		
		self.myLength += 8
		self.myBuffer = 0
		
	def AppendOneNote( self, note):
	
		self.myTrack += self.mySM.AppendNote( note, self.myBuffer, 2)			# half note
		self.myBuffer = 2	#half note rest
	
		self.myLength += 4
	
	def Terminate( self):

		self.myTrack += self.mySM.TerminateString( self.myBuffer)
		
	def Length( self):
	
		return self.myLength
	
	def Track( self):
	
		return self.myTrack
		
		
		
#test code
if __name__ == "__main__":

	t = NoteTranslator()
	sm = MidiStringMaker(t)
	tm = MidiTrackMaker(t,sm)
	
	tm.AppendCadence( t.GetMidiCodeForHumans("C4"), "major")
	tm.AppendOneNote( t.GetMidiCodeForHumans("E5"))
	tm.AppendCadence( t.GetMidiCodeForHumans("C4"), "minor")
	tm.AppendOneNote( t.GetMidiCodeForHumans("Eb5"))
	tm.Terminate()
	print tm.Track()
	print tm.Length()
