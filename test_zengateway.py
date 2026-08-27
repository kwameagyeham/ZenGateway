# test_zengateway.py
"""
Tests for ZenGateway module.
"""

import unittest
from zengateway import ZenGateway

class TestZenGateway(unittest.TestCase):
    """Test cases for ZenGateway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZenGateway()
        self.assertIsInstance(instance, ZenGateway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZenGateway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
