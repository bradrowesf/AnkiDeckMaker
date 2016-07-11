from nose.tools import *
from DeckMaker.note import Note


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():

	note = Note(57)
	assert_true('A4' in note.Names()) 
	assert_equal(note.MidiValue(), 57)
	assert_equal(note.ScaleValue(), 45)
	
	note = Note(48)
	assert_true('C4' in note.Names()) 
	assert_equal(note.MidiValue(), 48)
	assert_equal(note.ScaleValue(), 36)

	note = Note(104)
	assert_true('Ab8')
	assert_equal(note.MidiValue(), 104)
	assert_equal(note.ScaleValue(), 92)
