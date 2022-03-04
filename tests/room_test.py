import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Room Michael")
        self.new_possible_name = "My new room"
        self.new_possible_name_fail = "Room Michael"

    def test_room_has_name(self):
        self.assertEqual("Room Michael", self.room.name)

    def test_room_has_empty_list_of_guests(self):
        self.assertEqual([], self.room.list_of_guests)
    
    def test_room_has_empty_list_of_songs(self):
        self.assertEqual([], self.room.list_of_songs)

    def test_is_room_name_unique(self):
        new_name = self.room.is_room_name_unique(self.new_possible_name)
        self.assertEqual(True, new_name)
    
    # def test_room_has_been_created(self):
    #     result = self.room.create_a_room(room_name)
    #     self.assertEqual(result, Room(str(room_name)))