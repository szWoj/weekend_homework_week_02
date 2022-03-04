class Room:
    def __init__(self, name):
        self.name = name
        self.list_of_guests = []
        self.list_of_songs = []
        self.list_of_created_rooms = []

    def is_room_name_unique(self, name):
        if name not in self.list_of_created_rooms:
            return True
        return False
        
    # def create_a_room(self, room_name):
    #     return Room(str(room_name))