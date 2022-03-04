import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room Michael")

    def test_room_has_name(self):
        self.assertEqual("Room Michael", self.room.name)