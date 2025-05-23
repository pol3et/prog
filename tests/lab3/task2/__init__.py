import unittest
from .test_app import TestApp
from .test_ui import TestUI

def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestApp))
    suite.addTests(loader.loadTestsFromTestCase(TestUI))
    return suite