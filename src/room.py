class Room:
    def __init__(self, name):
        self.name = name
        self.list_of_guests = []
        self.list_of_songs = []
        
        

    def is_guest_checked_in(self, new_guest):
        for guest in self.list_of_guests:
            if new_guest.name == guest.name:
                return True
        return False
    
    def check_in_a_guest(self, guest):
        if not self.is_guest_checked_in(self):
            self.list_of_guests.append(guest)

    def check_out_a_guest(self, guest):
        if guest in self.list_of_guests:
            self.list_of_guests.remove(guest)
        else:
            self.list_of_guests

    
    def is_song_aleday_added(self, new_song):
        for song in self.list_of_songs:
            if new_song.name ==song.name:
                return True
        return False
    
    def add_song(self, song):
        if not self.is_song_aleday_added(self):
            self.list_of_songs.append(song)