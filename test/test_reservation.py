'''
This script contains all the unit test
pertaining to the Reservation class (reservation.py)
'''
import unittest
from src.customer import Customer
from src.hotel import Hotel
from src.reservation import Reservation


class TestReservationMethods(unittest.TestCase):
    """Unit tests for validating methods of the Reservation class"""
    def setUp(self):
        """This method is called before each test to set up the environment."""
        # Setup initial data for customers, hotels, and reservations
        self.hotels = [
            {"name": "Kyatt Hotel", "address": "786 Mountain View Rd",
                "rooms": 50},
            {"name": "Hotel Harris", "address": "456 Frontier Drive",
                "rooms": 100}
        ]

        # Create Customer objects instead of dictionaries
        self.customers = [
            Customer("Arian Reyes", "areyes@mitec.com", "859-587-7458"),
            Customer("Alex Fregoso", "afreg@gmail.com", "985-363-7485"),
            Customer("Carolyn Meyers", "meyersc@gmail.com", "857-665-8574"),
            Customer("Ruben Alvarez", "rubenalv@gmail.com", "985-454-7788")
        ]

        # Saving initial data to files
        Hotel.save_hotels(self.hotels)
        Customer.save_customers(self.customers)

        # Setup initial reservations based on the Customer objects
        self.initial_reservations = [
            {"hotel_name": "Kyatt Hotel", "customer": self.customers[1],
                "num_rooms": 2},
            {"hotel_name": "Kyatt Hotel", "customer": self.customers[2],
                "num_rooms": 1},
            {"hotel_name": "Hotel Harris", "customer": self.customers[3],
                "num_rooms": 2},
            {"hotel_name": "Hotel Harris", "customer": self.customers[0],
                "num_rooms": 1}
        ]

        for reservation in self.initial_reservations:
            Reservation.create_reservation(reservation["hotel_name"],
                                           reservation["customer"].name,
                                           reservation["num_rooms"])

    def tearDown(self):
        """This method is called after each test to clean up changes"""
        # Clean up customers, hotels, and reservations after each test
        for customer in self.customers:
            Customer.delete_customer(customer.name)
        for hotel in self.hotels:
            Hotel.delete_hotel(hotel["name"])

    def test_create_reservation(self):
        """Test creating a new reservation."""
        new_customer = Customer("John Doe", "johndoe@email.com",
                                "123-456-7890")
        Customer.create_customer(new_customer.name, new_customer.email,
                                 new_customer.phone_number)
        Reservation.create_reservation("Kyatt Hotel", "John Doe", 2)

        # Verify the reservation was created
        reservations = Reservation.load_reservations()
        self.assertTrue(any(r['customer']['name'] == "John Doe" and
                            r['hotel_name'] == "Kyatt Hotel"
                            for r in reservations))

    def test_cancel_reservation(self):
        """Test canceling a reservation"""
        # Verify the reservation was canceled
        reservations = Reservation.load_reservations()
        self.assertTrue(any(r['customer']['name'] == "Alex Fregoso" and
                            r['hotel_name'] == "Kyatt Hotel"
                            for r in reservations))

    def test_insufficient_rooms(self):
        """Test creating a reservation when there are not enough rooms."""
        result = Reservation.create_reservation("Kyatt Hotel",
                                                "Ruben Alvarez", 200)
        self.assertFalse(result)

    def test_modify_reservation(self):
        """Test modifying an existing reservation."""
        # Cancel previous reservation
        Reservation.cancel_reservation("Hotel Harris", "Ruben Alvarez", 2)

        # Create a new reservation for Ruben
        Reservation.create_reservation("Hotel Harris", "Ruben Alvarez", 1)
        reservations = Reservation.load_reservations()

        # Verify that the reservation was modified
        self.assertTrue(any(r['customer']['name'] == "Ruben Alvarez" and
                            r['hotel_name'] == "Hotel Harris"
                            for r in reservations))


if __name__ == '__main__':
    unittest.main()
