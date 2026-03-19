# controller/order_controller.py

from models import order_model, customer_model, product_model


def create_order(orders_db, customers_db, products_db, order_id, customer_id, product_id, quantity):
    """
    Validates data, calculates total, and creates a new order.
    Params:
        orders_db (dict): all registered orders
        customers_db (dict): all registered customers
        products_db (dict): all registered products
        order_id (str): unique order ID
        customer_id (str): ID of the customer
        product_id (str): ID of the product
        quantity (int): quantity purchased
    Returns:
        tuple: (bool, str, dict)
               bool -> True if created, False if error
               str  -> message result
               dict -> updated orders dictionary
    """
    # Check that no fields are empty
    if not order_id or not customer_id or not product_id or not quantity:
        return False, "All fields are required", orders_db

    # Check that quantity is valid
    if quantity <= 0:
        return False, "Quantity must be greater than zero", orders_db

    # Check that order ID does not already exist
    if order_model.order_exists(orders_db, order_id):
        return False, "Order ID already exists", orders_db

    # Check that customer exists
    if not customer_model.customer_exists(customers_db, customer_id):
        return False, "Customer not found", orders_db

    # Check that product exists
    product = product_model.get_product(products_db, product_id)
    if not product:
        return False, "Product not found", orders_db

    # Calculate total — price is at index 2 of the product tuple
    total = product[2] * quantity

    # Save to model
    updated_db = order_model.add_order(
        orders_db, order_id, customer_id, product, quantity, total
    )
    return True, f"Order '{order_id}' created. Total: ${total}", updated_db


def get_all_orders(orders_db, customers_db):
    """
    Gets all orders and validates there are orders to show.
    Params:
        orders_db (dict): all registered orders
        customers_db (dict): all registered customers
    Returns:
        tuple: (bool, str, dict)
               bool -> True if there are orders, False if empty
               str  -> message result
               dict -> the orders dictionary
    """
    all_orders = order_model.get_all_orders(orders_db)

    if not all_orders:
        return False, "No orders registered yet", {}

    return True, "Orders found", all_orders


def get_single_order(orders_db, customers_db, order_id):
    """
    Gets one specific order by its ID.
    Params:
        orders_db (dict): all registered orders
        customers_db (dict): all registered customers
        order_id (str): the ID to search
    Returns:
        tuple: (bool, str, dict)
               bool -> True if found, False if not
               str  -> message result
               dict -> the single order or empty dict
    """
    if not order_model.order_exists(orders_db, order_id):
        return False, f"Order '{order_id}' not found", {}

    order = orders_db[order_id]
    return True, "Order found", order
