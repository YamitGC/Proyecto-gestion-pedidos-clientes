# controller/customer_controller.py

from models import customer_model


def register_customer(customers_db, customer_id, name, email):
    """
    Validates and registers a new customer.
    Params:
        customers_db (dict): current customers dictionary
        customer_id (str): unique ID
        name (str): customer name
        email (str): customer email
    Returns:
        tuple: (bool, str, dict)
               bool -> True if registered, False if error
               str  -> message result
               dict -> updated customers dictionary
    """
    # First check that no fields are empty
    if not customer_id or not name or not email:
        return False, "All fields are required", customers_db

    # Then check if customer already exists
    if customer_model.customer_exists(customers_db, customer_id):
        return False, "Customer ID already exists", customers_db

    # Save to model
    updated_db = customer_model.add_customer(customers_db, customer_id, name, email)
    return True, f"Customer '{name}' registered successfully", updated_db
