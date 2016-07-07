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
	assert_equal(translator.GetMidiCodeHexString("E5"),"4c")
	assert_equal(translator.GetMidiCodeHexString("C1"),"18")
	assert_equal(translator.GetMidiCodeHexString("Ab6"),"5c")
	assert_equal(translator.GetMidiCodeHexString("Gb7"),"66")
	assert_equal(translator.GetMidiCodeHexString("D#2"),"27")
	pass

def test_GetTriadCodes():
	translator = NoteTranslator()
	assert_equal(translator.GetTriadCodes( "C4", "minor", 3),[60, 65, 68])
	assert_equal(translator.GetTriadCodes( "Ab2", "major", 2),[44, 52, 47])
	assert_equal(translator.GetTriadCodes( "G#6", "minor", 1),[92, 95, 99])


def test_GetTriadHexCodeStrings():
	translator = NoteTranslator()
	assert_equal(translator.GetTriadHexCodeStrings( "C4", "major", 1),['3c', '40', '43'])
	assert_equal(translator.GetTriadHexCodeStrings( "Ab2", "major", 2),['2c', '34', '2f'])
	assert_equal(translator.GetTriadHexCodeStrings( "G#6", "minor", 1),['5c', '5f', '63'])