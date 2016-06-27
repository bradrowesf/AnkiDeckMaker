try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Anki Deck Maker',
    'author': 'Bradley Rowe',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose','json'],
    'packages': ['DeckMaker'],
    'scripts': [],
    'name': 'DeckMaker'
}

setup(**config)
