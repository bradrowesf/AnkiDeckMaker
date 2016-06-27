import argparse

from deckoptions import DeckOptions
from deckconfig import Configuration

options = DeckOptions(argparse.ArgumentParser())
print "Loading config file: " + options.pathToConfig()

configs = Configuration (options.pathToConfig())
print configs.getTestValue()
