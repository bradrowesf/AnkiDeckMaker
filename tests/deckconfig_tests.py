from nose.tools import *
from DeckMaker.deckconfig import Configuration

class TestConfiguration(object):
    @classmethod
    def setup_class(self):
       self.config = Configuration("bin/defaultconfig.json")

    @classmethod
    def teardown_class(self):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_UpperRange(self):
        assert_equal(self.config.getUpperRange(), "E4")
        
    def test_LowerRange(self):
		assert_equal(self.config.getLowerRange(), "E2")