# Function that requests order data from the user
def pedir_datos_pedido():
    """
    Requests order details from the user.
    Returns:
        tuple: (pedido_id, cliente_id, producto_id, cantidad)
    """
    print("--- Registro de Nuevo Pedido ---")
    
    # Input collection from the user
    pedido_id = input("Escribe el ID del pedido: ")
    cliente_id = input("Escribe el ID del cliente: ")
    producto_id = input("Escribe el ID del producto: ")
    
    # Converting quantity to integer for calculations
    cantidad = int(input("Escribe la cantidad: "))
    
    # Returns data as a tuple to comply with technical constraints
    return pedido_id, cliente_id, producto_id, cantidad

# Function that returns the result message to the user
def mostrar_resultado_pedido(resultado):
    """
    Returns the status message of the order creation.
    Parameters:
        resultado (dict or None): result of the order creation logic
    Returns:
        str: formatted message to be displayed
    """
    # Validation logic based on the model's return value
    if resultado is None:
        # Message if the ID already exists in the dictionary
        return "Error: El pedido ya existe o no se pudo procesar."
    else:
        # Success message for correct registration and calculation
        return "Pedido creado exitosamente con el cálculo de total incluido."