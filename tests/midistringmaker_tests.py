from nose.tools import *
from DeckMaker.midistringmaker import MidiStringMaker
from DeckMaker.notetranslator import NoteTranslator

class TestMidiStringMaker(object):
    @classmethod
    def setup_class(self):
	
		self.translator = NoteTranslator()
		self.stringMaker = MidiStringMaker(self.translator)

    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

	def test_KeyDown(self):
		assert_equal(self.stringMaker.KeyDown( "E5", 3, False), "E 2880 90 4c 60")
		assert_equal(self.stringMaker.KeyDown( "D#2", 17, True), "E 16320 90 27 60\n")
		
	def test_KeyUp(self):
		assert_equal(self.stringMaker.KeyUp( "G#4", 2, True), "E 1920 80 44 60\n")
		assert_equal(self.stringMaker.KeyUp( "D#2", 17, False), "E 13440 80 1b 60")

	def test_AppendNote(self):
		assert_equal(self.stringMaker.AppendNote( "E#5", 12, 3), "E 11520 90 4d 60\nE 2880 80 4d 60")
		assert_equal(self.stringMaker.AppendNote( "A#2", 3, 7), "E 2880 90 2e 60\nE 6720 80 2e 60")
