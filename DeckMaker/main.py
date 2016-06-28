import argparse

from deckoptions import DeckOptions
from deckconfig import Configuration
from notetranslator import NoteTranslator

options = DeckOptions()
print "Loading config file: " + options.pathToConfig()

configs = Configuration (options.pathToConfig())

translator = NoteTranslator()
translator.DumpTable()