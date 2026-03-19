# models/customer_model.py

def add_customer(customers_db, customer_id, name, email):
    """
    Adds a new customer to the database.
    Params:
        customers_db (dict): the current customers dictionary
        customer_id (str): unique customer ID
        name (str): customer full name
        email (str): customer email
    Returns:
        dict: updated customers dictionary
    """
    customers_db[customer_id] = {
        "name": name,
        "email": email
    }
    return customers_db


def customer_exists(customers_db, customer_id):
    """
    Checks if a customer already exists.
    Params:
        customers_db (dict): the current customers dictionary
        customer_id (str): ID to check
    Returns:
        bool: True if exists, False otherwise
    """
    return customer_id in customers_db


def get_all_customers(customers_db):
    """
    Returns all registered customers.
    Params:
        customers_db (dict): the current customers dictionary
    Returns:
        dict: all customers
    """
    return customers_db
