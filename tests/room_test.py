import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room1 = Room("Room Michael")
        self.room2 = Room("Room Robbie")
        
        self.guest1 = Guest("Szymon Wojdyla")
        self.guest2 = Guest("Sebastian Wojdyla")
        
        self.song1 = Song("Yellow Submarine")
        self.song1 = Song("Yellow Submarine")
        self.room1.list_of_guests = [self.guest1]
        self.room2.list_of_guests = []
        
        #self.new_possible_name = "My new room"
        #self.new_possible_name_fail = "Room Michael"
        #self.list_of_created_rooms = [self.room]

    def test_room_has_name(self):
        self.assertEqual("Room Michael", self.room1.name)

    def test_room_has_empty_list_of_guests(self):
        self.assertEqual([], self.room2.list_of_guests)
    
    def test_room_has_empty_list_of_songs(self):
        self.assertEqual([], self.room1.list_of_songs)

    def test_is_guest_checked_in(self):
        result = self.room1.is_guest_checked_in(self.guest1)
        self.assertEqual(result, True)

    def test_is_guest_not_checked_in(self):
        result = self.room2.is_guest_checked_in(self.guest1)
        self.assertEqual(result, False)

    def test_check_in_a_guest(self):
        self.room2.check_in_a_guest(self.guest1)
        self.assertEqual([self.guest1], self.room2.list_of_guests)
    
    def test_check_out_a_guest(self):
        self.room1.check_out_a_guest(self.guest1)
        self.assertEqual([], self.room1.list_of_guests)

    def test_check_out_a_guest_not_possible(self):
        self.room1.check_out_a_guest(self.guest2)
        self.assertEqual([self.guest1], self.room1.list_of_guests)
    
    
    # def test_is_song_alreday_added(self):
    #     pass

    
    # def test_is_room_name_unique(self):
    #     new_name = self.room.is_room_name_unique(self.new_possible_name)
    #     self.assertEqual(True, new_name)
    
    # def test_is_room_name_unique_fail(self):
    #     new_name = self.room.is_room_name_unique(self.new_possible_name_fail)
    #     self.assertEqual(False, new_name)
    
    # def test_room_has_been_created(self):
    #     result = self.room.create_a_room(room_name)
    #     self.assertEqual(result, Room(str(room_name)))