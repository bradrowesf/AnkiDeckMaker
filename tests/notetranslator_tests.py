from nose.tools import *
from DeckMaker.notetranslator import NoteTranslator


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
	translator = NoteTranslator()
	assert_equal(translator.GetMidiCode("E5"),76)
	assert_equal(translator.GetMidiCode("C1"),24)
	assert_equal(translator.GetMidiCode("Ab6"),92)
	assert_equal(translator.GetMidiCode("Gb7"),102)
	assert_equal(translator.GetMidiCode("D#2"),39)
	pass
