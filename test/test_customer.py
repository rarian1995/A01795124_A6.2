'''
This script contains all the unit test
pertaining to the Customer class (customer.py)
'''
import unittest
from src.customer import Customer


class TestCustomerMethods(unittest.TestCase):
    """Unit tests for validating methods of the Customer class"""
    def setUp(self):
        """This method is called before each test to set up the environment"""
        # Setup initial customer data
        self.initial_data = [
            {"name": "Arian Reyes", "email": "areyes@mitec.com",
             "phone_number": "859-587-7458"},
            {"name": "Alex Fregoso", "email": "afreg@gmail.com",
             "phone_number": "985-363-7485"},
            {"name": "Carolyn Meyers", "email": "meyersc@gmail.com",
             "phone_number": "857-665-8574"},
            {"name": "Ruben Alvarez", "email": "rubenalv@gmail.com",
             "phone_number": "985-454-7788"}
        ]

        for customer in self.initial_data:
            Customer.create_customer(customer["name"], customer["email"],
                                     customer["phone_number"])

    def tearDown(self):
        """This method is called after each test to clean up changes"""
        # Clean up customer data after each test
        for customer in self.initial_data:
            Customer.delete_customer(customer["name"])

    def test_create_customer(self):
        """Test creating a new customer"""
        Customer.create_customer("John Doe", "johndoe@email.com",
                                 "123-456-7890")
        customers = Customer.get_customers()
        self.assertTrue(any(c.name == "John Doe" for c in customers))

    def test_delete_customer(self):
        """Test deleting a customer."""
        Customer.create_customer("Test Customer", "test@email.com",
                                 "987-654-3210")
        Customer.delete_customer("Test Customer")
        customers = Customer.get_customers()
        self.assertFalse(any(c.name == "Test Customer" for c in customers))

    def test_display_customer_info(self):
        """Test displaying customer info."""
        Customer.create_customer("Test Display", "display@email.com",
                                 "555-555-5555")
        Customer.display_customer_info("Test Display")

    def test_modify_customer_info(self):
        """Test modifying customer info"""
        Customer.create_customer("Modify Me", "modify@email.com",
                                 "111-222-3333")
        Customer.modify_customer_info("Modify Me",
                                      new_email="modified@email.com")
        customers = Customer.get_customers()
        self.assertTrue(any(c.email == "modified@email.com"
                            for c in customers))


if __name__ == '__main__':
    unittest.main()
