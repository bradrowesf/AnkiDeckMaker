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
	
def test_hex():
	translator = NoteTranslator()
	assert_equal(translator.GetMidiNoteHexString("E5"),"4c")
	assert_equal(translator.GetMidiNoteHexString("C1"),"18")
	assert_equal(translator.GetMidiNoteHexString("Ab6"),"5c")
	assert_equal(translator.GetMidiNoteHexString("Gb7"),"66")
	assert_equal(translator.GetMidiNoteHexString("D#2"),"27")
	pass

