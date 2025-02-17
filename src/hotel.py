'''
This script is focused on generating the Hotel class.
The methods pertaining containing the Hotel class are
a. Creating a Hotel
b. Deleting a Hotel
c. Displaying Hotel Information
d. Modifying Hotel Information
e. Reserving a Room
f. Canceling a Reservation
'''
import json


class Hotel:
    """
    A class representing a hotel with a name,
    address, and number of rooms.
    """
    def __init__(self, name, address, rooms):
        """
        Initializes a new Hotel object with the specified name,
        address, and number of rooms
        """
        self.name = name
        self.address = address
        self.rooms = rooms

    @staticmethod
    def create_hotel(name, address, rooms):
        '''This method is used to create a hotel'''
        hotels = Hotel.load_hotels()
        new_hotel = Hotel(name, address, rooms)
        hotels.append(new_hotel.to_dict())
        Hotel.save_hotels(hotels)

    @staticmethod
    def delete_hotel(hotel_name):
        '''This method is used to delete a hotel'''
        hotels = Hotel.load_hotels()
        hotels = [h for h in hotels if h["name"] != hotel_name]
        Hotel.save_hotels(hotels)

    def display_info(self):
        '''This method is used to display hotel information'''
        return f"Hotel:{self.name},Address:{self.address},Rooms:{self.rooms}"

    def to_dict(self):
        """Converts the object into a dictionary with keys"""
        return {"name": self.name, "address": self.address,
                "rooms": self.rooms}

    @classmethod
    def from_dict(cls, data):
        """Creates an instance of the Hotel class from a dictionary"""
        return cls(data["name"], data["address"], data["rooms"])

    @staticmethod
    def display_hotel_info(hotel_name):
        """Displays the information of a hotel by its name"""
        hotels = Hotel.load_hotels()
        for hotel in hotels:
            if hotel["name"] == hotel_name:
                print(Hotel.from_dict(hotel).display_info())

    @staticmethod
    def modify_hotel_info(hotel_name, new_name=None,
                          new_address=None, new_rooms=None):
        """Modifies the information of an existing hotel"""
        hotels = Hotel.load_hotels()
        for hotel in hotels:
            if hotel["name"] == hotel_name:
                if new_name:
                    hotel["name"] = new_name
                if new_address:
                    hotel["address"] = new_address
                if new_rooms is not None:
                    hotel["rooms"] = new_rooms
                Hotel.save_hotels(hotels)
                break

    def reserve_room(self, num_rooms):
        """Reserves rooms at the hotel if there are enough available"""
        if self.rooms >= num_rooms:
            self.rooms -= num_rooms
            return True
        return False

    def cancel_reservation(self, num_rooms):
        """This method is used to cancel reservations"""
        self.rooms += num_rooms

        # Load the hotels
        hotels = Hotel.load_hotels()

        # Update the specific hotel in the list
        for hotel in hotels:
            if hotel["name"] == self.name:
                hotel["rooms"] = self.rooms

        # Save the updated list of hotels
        Hotel.save_hotels(hotels)

    @staticmethod
    def load_hotels():
        """Loads the list of hotels from the 'hotels.json' file"""
        try:
            with open('hotels.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_hotels(hotels):
        """Saves the list of hotels to the 'hotels.json' file."""
        with open('hotels.json', 'w', encoding='utf-8') as file:
            json.dump(hotels, file, indent=4)

    @staticmethod
    def get_hotels():
        """Returns the list of hotels."""
        return Hotel.load_hotels()
