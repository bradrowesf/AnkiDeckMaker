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
		
	def test_ChordDown(self):
		notes = []
		notes.append(self.t.GetMidiCodeForHumans("Gb5"))
		notes.append(self.t.GetMidiCodeForHumans("C#2"))
		notes.append(self.t.GetMidiCodeForHumans("A3"))
		assert_equal(self.sm.ChordDown( notes, 2), "E 1920 90 4e 60\nE 1920 90 25 60\nE 1920 90 2d 60\n")
		assert_equal(self.sm.ChordDown( notes, 2), "E 1920 90 4e 60\nE 1920 90 25 60\nE 1920 90 2d 60\n")
		
		notes = []
		notes.append(self.t.GetMidiCodeForHumans("A#2"))
		notes.append(self.t.GetMidiCodeForHumans("F2"))
		notes.append(self.t.GetMidiCodeForHumans("E4"))
	
		notes = []
		notes.append(self.t.GetMidiCodeForHumans("Cb5"))
		notes.append(self.t.GetMidiCodeForHumans("C#2"))
		notes.append(self.t.GetMidiCodeForHumans("G7"))

	def test_ChordUp(self):
		notes = []
	
	def test_AppendChord(self):
	
		notes = []
	