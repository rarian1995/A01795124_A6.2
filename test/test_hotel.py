'''
This script contains all the unit test
pertaining to the Hotel class (hotel.py)
'''
import unittest
import json
from src.hotel import Hotel


class TestHotelMethods(unittest.TestCase):
    """Unit tests for validating methods of the Hotel class"""
    def setUp(self):
        """This method is called before each test to set up the environment"""
        # Initialized file with predefined hotels
        self.hotels_data = [
            {"name": "Hotel Harris", "address": "456 Frontier Drive",
                "rooms": 100},
            {"name": "Kyatt Hotel", "address": "786 Mountain View Rd",
                "rooms": 50}
        ]
        with open('hotels.json', 'w', encoding='utf-8') as file:
            json.dump(self.hotels_data, file, indent=4)

    def tearDown(self):
        """This method cleans up changes after eery test"""
        with open('hotels.json', 'w', encoding='utf-8') as file:
            json.dump(self.hotels_data, file, indent=4)

    def test_create_hotel(self):
        '''Test for creation of hotel'''
        # Create a new hotel
        Hotel.create_hotel("Test Hotel", "123 Test St", 75)

        # Load the updated hotels from the file
        hotels = Hotel.get_hotels()
        hotel_names = [hotel["name"] for hotel in hotels]

        self.assertIn("Test Hotel", hotel_names)

    def test_reserve_room(self):
        '''Test for reserve room functionality'''
        hotel = Hotel("Hotel Harris", "456 Frontier Drive", 100)

        # Reserve rooms
        result = hotel.reserve_room(20)
        self.assertTrue(result)
        self.assertEqual(hotel.rooms, 80)

    def test_delete_hotel(self):
        '''Test for Hotel Deletion Functionality'''
        # Ensure Hotel Harris exists in the initial data
        hotels = Hotel.get_hotels()
        hotel_names = [hotel["name"] for hotel in hotels]
        self.assertIn("Hotel Harris", hotel_names)

        # Delete the hotel
        Hotel.delete_hotel("Hotel Harris")

        # Check if the hotel was deleted
        hotels = Hotel.get_hotels()
        hotel_names = [hotel["name"] for hotel in hotels]
        self.assertNotIn("Hotel Harris", hotel_names)

    def test_modify_hotel_info(self):
        '''Tests functionality for Modifications to Hotel Information'''
        # Modify hotel information
        Hotel.modify_hotel_info("Kyatt Hotel", new_name="Kyatt Grand",
                                new_address="800 Mountain View Rd",
                                new_rooms=60)

        hotels = Hotel.get_hotels()
        hotel_names = [hotel["name"] for hotel in hotels]

        # Assert that the modification has been done
        self.assertIn("Kyatt Grand", hotel_names)


if __name__ == '__main__':
    unittest.main()
