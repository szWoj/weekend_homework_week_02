class Room:
    def __init__(self, name):
        self.name = name
        self.list_of_guests = []
        self.list_of_songs = []
        #self.list_of_created_rooms = []

    # def is_room_name_unique(self, name):
    #     for room in self.list_of_created_rooms:
    #         if room.name == name:
    #             return False
    #     return True

    # def create_a_room(self, room_name):
    #     return Room(str(room_name))

    def is_guest_checked_in(self, new_guest):
        for guest in self.list_of_guests:
            if new_guest.name == guest.name:
                return True
        return False
    
    # def check_in_a_guest(self, guest):
    #     self.list_of_guests.append(guest)

    def check_out_a_guest(self, guest):
        pass

    def add_song(self, song):
        pass