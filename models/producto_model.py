# Dictionary to store all registered products
productos = {}

# Function that registers a new product in the products dictionary
def registrar_producto(productos, producto_id, nombre_producto, precio_unidad):
    """
    Registers a new product in the system.
    Parameters:
        productos (dict): dictionary of existing products
        producto_id (str): unique product identifier
        nombre_producto (str): name of the product
        precio_unidad (float): unit price of the product
    Returns:
        dict: updated products dictionary
    """
    if producto_id in productos:
        return None
    else:
        productos[producto_id] = (producto_id, nombre_producto, precio_unidad)
    return productos