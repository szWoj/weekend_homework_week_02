import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Mark Robson")
    
    def test_guest_has_name(self):
        self.assertEqual("Mark Robson", self.guest.name)