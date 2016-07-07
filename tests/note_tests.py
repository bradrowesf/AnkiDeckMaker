from nose.tools import *
from DeckMaker.note import Note


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():

	note = Note(57)
	assert_equal(note.Names(), ['A4']) 
	assert_equal(note.MidiValue(), 57)
	assert_equal(note.ScaleValue(), 36)