def add_product(products_db, product_id, product_name, unit_price):
    """
    Adds a new product to the database as a tuple.
    Params:
        products_db (dict): the current products dictionary
        product_id (str): unique product ID
        product_name (str): name of the product
        unit_price (float): unit price of the product
    Returns:
        dict: updated products dictionary
    """
    products_db[product_id] = (product_id, product_name, unit_price)
    return products_db


def product_exists(products_db, product_id):
    """
    Checks if a product already exists.
    Params:
        products_db (dict): the current products dictionary
        product_id (str): ID to check
    Returns:
        bool: True if exists, False otherwise
    """
    return product_id in products_db


def get_product(products_db, product_id):
    """
    Returns a single product tuple by ID.
    Params:
        products_db (dict): the current products dictionary
        product_id (str): ID to search
    Returns:
        tuple: (product_id, product_name, unit_price) or None
    """
    return products_db.get(product_id)


def get_all_products(products_db):
    """
    Returns all registered products.
    Params:
        products_db (dict): the current products dictionary
    Returns:
        dict: all products
    """
    return products_db
