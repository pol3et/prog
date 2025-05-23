import unittest

from .test_database import TestDatabase
from .test_movie import TestMovie
from .test_user import TestUser
from .test_recsys import TestRecSys
from .test_ui import TestUI


def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestMovie))
    suite.addTests(loader.loadTestsFromTestCase(TestUser))
    suite.addTests(loader.loadTestsFromTestCase(TestRecSys))
    suite.addTests(loader.loadTestsFromTestCase(TestUI))
    return suite 