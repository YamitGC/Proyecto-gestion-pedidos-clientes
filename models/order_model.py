# models/order_model.py

def add_order(orders_db, order_id, customer_id, product_tuple, quantity, total):
    """
    Adds a new order to the database.
    Params:
        orders_db (dict): the current orders dictionary
        order_id (str): unique order ID
        customer_id (str): ID of the customer who made the order
        product_tuple (tuple): product data (product_id, name, price)
        quantity (int): quantity purchased
        total (float): total price of the order
    Returns:
        dict: updated orders dictionary
    """
    orders_db[order_id] = {
        "customer_id": customer_id,
        "product": product_tuple,
        "quantity": quantity,
        "total": total
    }
    return orders_db


def get_all_orders(orders_db):
    """
    Returns all registered orders.
    Params:
        orders_db (dict): the current orders dictionary
    Returns:
        dict: all orders
    """
    return orders_db


def get_order_total(order):
    """
    Returns the total of a single order.
    Params:
        order (dict): a single order dictionary
    Returns:
        float: the total of that order
    """
    return order["total"]


def order_exists(orders_db, order_id):
    """
    Checks if an order already exists.
    Params:
        orders_db (dict): the current orders dictionary
        order_id (str): the order ID to check
    Returns:
        bool: True if exists, False otherwise
    """
    return order_id in orders_db
