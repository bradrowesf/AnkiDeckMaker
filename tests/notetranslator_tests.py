from nose.tools import *
from DeckMaker.notetranslator import NoteTranslator


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
	t = NoteTranslator()
	assert_equal(t.GetMidiCodeForHumans("E5"),64)
	assert_equal(t.GetMidiCodeForHumans("C1"),12)
	assert_equal(t.GetMidiCodeForHumans("Ab6"),80)
	assert_equal(t.GetMidiCodeForHumans("Gb7"),90)
	assert_equal(t.GetMidiCodeForHumans("D#2"),27)
	pass
	
def test_hex():
	t = NoteTranslator()
	assert_equal(t.GetHexString(t.GetMidiCodeForHumans("E5")),"40")
	assert_equal(t.GetHexString(t.GetMidiCodeForHumans("C1")),"c")
	assert_equal(t.GetHexString(t.GetMidiCodeForHumans("Ab6")),"50")
	assert_equal(t.GetHexString(t.GetMidiCodeForHumans("Gb7")),"5a")
	assert_equal(t.GetHexString(t.GetMidiCodeForHumans("D#2")),"1b")
	pass

def test_GetTriadCodes():
	t = NoteTranslator()
	assert_equal(t.GetTriadCodes( t.GetMidiCodeForHumans("C4"), "minor", 3),[48, 53, 56])
	assert_equal(t.GetTriadCodes( t.GetMidiCodeForHumans("Ab2"), "major", 2),[32, 40, 35])
	assert_equal(t.GetTriadCodes( t.GetMidiCodeForHumans("G#6"), "minor", 1),[80, 83, 87])


def test_GetTriadHexCodeStrings():
	t = NoteTranslator()
	assert_equal(t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("C4"), "major", 1),['30', '34', '37'])
	assert_equal(t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("Ab2"), "major", 2),['20', '28', '23'])
	assert_equal(t.GetTriadHexCodeStrings( t.GetMidiCodeForHumans("G#6"), "minor", 1),['50', '53', '57'])