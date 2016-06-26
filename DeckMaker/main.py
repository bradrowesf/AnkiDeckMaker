import argparse

from deckoptions import DeckOptions

options = DeckOptions(argparse.ArgumentParser())
print options.pathToConfig()
