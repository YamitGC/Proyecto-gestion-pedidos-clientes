# controller/product_controller.py

from models import product_model


def register_product(products_db, product_id, product_name, unit_price):
    """
    Validates and registers a new product.
    Params:
        products_db (dict): current products dictionary
        product_id (str): unique product ID
        product_name (str): name of the product
        unit_price (float): unit price of the product
    Returns:
        tuple: (bool, str, dict)
               bool -> True if registered, False if error
               str  -> message result
               dict -> updated products dictionary
    """
    # Check that no fields are empty
    if not product_id or not product_name or not unit_price:
        return False, "All fields are required", products_db

    # Check that price is a valid positive number
    if unit_price <= 0:
        return False, "Price must be greater than zero", products_db

    # Check if product already exists
    if product_model.product_exists(products_db, product_id):
        return False, "Product ID already exists", products_db

    # Save to model
    updated_db = product_model.add_product(products_db, product_id, product_name, unit_price)
    return True, f"Product '{product_name}' registered successfully", updated_db
