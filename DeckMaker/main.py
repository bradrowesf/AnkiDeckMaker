import argparse

from deckoptions import DeckOptions
from deckconfig import Configuration
from notetranslator import NoteTranslator
from filemanager import FileManager

options = DeckOptions()
print "Loading config file: " + options.pathToConfig()

configs = Configuration (options.pathToConfig())

translator = NoteTranslator()
translator.DumpNotes()

fileManager = FileManager(options.pathToOutput())
#fileManager.Write()


# lets make a chord
