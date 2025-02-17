'''
This script is focused on generating the Customer class
The methods pertaining containing the Customer class are
a. Creating a Customer
b. Deleting a Customer
c. Displaying Customer Information
d. Modifying Customer Information
'''
import json


class Customer:
    """A class representing a customer with name, email, and phone number."""
    def __init__(self, name, email, phone_number):
        """
        Initializes a new Customer object with the specified name,
        email, and phone number.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def to_dict(self):
        """Convert Customer object to dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }

    @classmethod
    def from_dict(cls, data):
        """Creates an instance of the class from a dictionary."""
        return cls(data["name"], data["email"], data["phone_number"])

    @staticmethod
    def create_customer(name, email, phone_number):
        """Creates a new customer and saves it to the JSON file."""
        customer = Customer(name, email, phone_number)
        customers = Customer.load_customers()
        customers.append(customer)
        Customer.save_customers(customers)

    @staticmethod
    def delete_customer(name):
        """Deletes a customer by name."""
        customers = Customer.load_customers()
        # Filter customers, keep only those who do not match the name
        customers = [c for c in customers if c.name != name]
        Customer.save_customers(customers)

    @staticmethod
    def display_customer_info(name):
        """Displays customer information."""
        customers = Customer.load_customers()
        for customer in customers:
            if customer.name == name:
                print(customer.display_info())

    @staticmethod
    def modify_customer_info(name, new_name=None,
                             new_email=None, new_phone=None):
        """Modifies customer information."""
        customers = Customer.load_customers()
        for customer in customers:
            if customer.name == name:  # Match by customer name
                if new_name:
                    customer.name = new_name
                if new_email:
                    customer.email = new_email
                if new_phone:
                    customer.phone_number = new_phone
                Customer.save_customers(customers)
                break

    def display_info(self):
        """Displays the customer information in a readable format."""
        return f"Name:{self.name},Email:{self.email},Phone:{self.phone_number}"

    @staticmethod
    def load_customers():
        """Loads the list of customers from a JSON file."""
        try:
            with open('customers.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Convert each dictionary to a Customer object
                return [Customer.from_dict(customer) for customer in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    @staticmethod
    def save_customers(customers):
        """Save customers to file."""
        with open('customers.json', 'w', encoding='utf-8') as file:
            # Save list of customer dictionaries
            json.dump([customer.to_dict()
                       for customer in customers], file, indent=4)

    @staticmethod
    def get_customers():
        """Returns a list of all customers."""
        return Customer.load_customers()
