from nose.tools import *
from DeckMaker.midistringmaker import MidiStringMaker
from DeckMaker.notetranslator import NoteTranslator

class TestMidiStringMaker(object):
    
	def __init__(self):

		self.t = NoteTranslator()
		self.sm = MidiStringMaker(self.t)
	
 	def test_KeyDown(self):
		assert_equal(self.sm.KeyDown( self.t.GetMidiCodeForHumans("E5"), 3), "E 2880 90 4c 60\n")
		assert_equal(self.sm.KeyDown( self.t.GetMidiCodeForHumans("D#2"), 17), "E 16320 90 27 60\n")
		
	def test_KeyUp(self):
		assert_equal(self.sm.KeyUp( self.t.GetMidiCodeForHumans("G#4"), 2), "E 1920 80 44 60\n")
		assert_equal(self.sm.KeyUp( self.t.GetMidiCodeForHumans("D#2"), 17), "E 16320 80 27 60\n")

	def test_AppendNote(self):
		assert_equal(self.sm.AppendNote( self.t.GetMidiCodeForHumans("E#5"), 12, 3), "E 11520 90 4d 60\nE 2880 80 4d 60\n")
		assert_equal(self.sm.AppendNote( self.t.GetMidiCodeForHumans("A#2"), 3, 7), "E 2880 90 22 60\nE 6720 80 22 60\n")
		
	def GetChordNotes( self, humanNotes):
		# Utility method for Chord Tests
	
		outNotes = []
		for note in humanNotes:
			outNotes.append(self.t.GetMidiCodeForHumans(note))
			
		return outNotes
	
	def test_ChordDown(self):
		notes = self.GetChordNotes(["Gb5","C#2","A3"])
		assert_equal(self.sm.ChordDown( notes, 2), "E 1920 90 4e 60\nE 1920 90 25 60\nE 1920 90 2d 60\n")
		
		notes = self.GetChordNotes(["A#2","F2","E4"])
		assert_equal(self.sm.ChordDown( notes, 3), "E 2880 90 22 60\nE 2880 90 29 60\nE 2880 90 40 60\n")
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.ChordDown( notes, 5), "E 4800 90 47 60\nE 4800 90 25 60\nE 4800 90 67 60\n")

	def test_ChordUp(self):
		notes = self.GetChordNotes(["Gb5","C#2","A3"])
		assert_equal(self.sm.ChordUp( notes, 4), "E 3840 80 4e 60\nE 3840 80 25 60\nE 3840 80 2d 60\n")
		
		notes = self.GetChordNotes(["A#2","F2","E4"])
		assert_equal(self.sm.ChordUp( notes, 7.5), "E 7200 80 22 60\nE 7200 80 29 60\nE 7200 80 40 60\n")
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.ChordUp( notes, 3.5), "E 3360 80 47 60\nE 3360 80 25 60\nE 3360 80 67 60\n")
	
	def test_AppendChord(self):
	
		notes = self.GetChordNotes(["Cb5","C#2","G7"])
		assert_equal(self.sm.AppendChord( notes, 3.5, 2),"E 3360 90 47 60\nE 3360 90 25 60\nE 3360 90 67 60\nE 1920 80 47 60\nE 1920 80 25 60\nE 1920 80 67 60\n")