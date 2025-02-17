'''
This script is focused on generating the Reservation class
The methods pertaining containing the Reservation class are
a. Creating a Reservation
b. Canceling a Reservation
'''
import json
import logging
from src.hotel import Hotel
from src.customer import Customer

logging.basicConfig(level=logging.DEBUG)


class Reservation:
    """A class representing a reservation made by a customer at a hotel."""
    def __init__(self, hotel_name, customer, num_rooms):
        """Initializes a new Reservation object."""
        self.hotel_name = hotel_name
        self.customer = customer
        self.num_rooms = num_rooms

    def to_dict(self):
        """Convert Reservation object to dictionary."""
        return {
            "hotel_name": self.hotel_name,
            "customer": self.customer.to_dict(),
            "num_rooms": self.num_rooms
        }

    @staticmethod
    def create_reservation(hotel_name, customer_name, num_rooms):
        """Creates a reservation for a customer at a hotel."""
        hotels = Hotel.load_hotels()
        customers = Customer.load_customers()

        hotel = next((h for h in hotels if h['name'] == hotel_name), None)
        customer = next((c for c in customers
                         if c.name == customer_name), None)

        if hotel and customer:
            if hotel["rooms"] >= num_rooms:
                reservation = Reservation(hotel_name, customer, num_rooms)
                Reservation._save_reservation(reservation)
                hotel["rooms"] -= num_rooms
                Hotel.save_hotels(hotels)
                return True
        return False

    @staticmethod
    def _save_reservation(reservation):
        """Save reservation to the reservations file."""
        reservations = Reservation._load_reservations()
        reservations.append(reservation.to_dict())
        with open('reservations.json', 'w', encoding='utf-8') as file:
            json.dump(reservations, file, indent=4)
            return []

    @staticmethod
    def cancel_reservation(hotel_name, customer_name, num_rooms):
        """Cancel a reservation."""
        hotels = Hotel.get_hotels()
        reservations = Reservation._load_reservations()
        # Cancelling the reservation and adjust rooms
        for hotel in hotels:
            if hotel["name"] == hotel_name:
                hotel_instance = Hotel.from_dict(hotel)
                hotel_instance.cancel_reservation(num_rooms)
                hotel["rooms"] = hotel_instance.rooms

                # Removing the reservation from the list
                reservations = [r for r in reservations if not (
                                r['customer']['name'] == customer_name and
                                r['hotel_name'] == hotel_name)]

    @staticmethod
    def _load_reservations():
        """Loads reservations from a file and handles errors gracefully."""
        try:
            # Attempt to open and read the reservations file
            with open('reservations.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file is not found, log the error and return an empty list
            logging.error("Reservations file not found.")
            return []
        except json.JSONDecodeError:
            # If the JSON file is malformed, log the error
            logging.error("Error decoding JSON from reservations file.")
            return []

    @staticmethod
    def load_reservations():
        """Public method to load reservations with error handling."""
        return Reservation._load_reservations()
