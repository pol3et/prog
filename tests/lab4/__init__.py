import unittest

from .test_order import TestOrder
from .test_processor import TestOrderProcessor


def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestOrder))
    suite.addTests(loader.loadTestsFromTestCase(TestOrderProcessor))
    return suite
