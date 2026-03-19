from models.pedido_model import crear_pedido
from view.pedido_view import pedir_datos_pedido, mostrar_resultado_pedido

# Function that controls the product registration flow [cite: 42]
def controlador_pedido(pedidos, clientes, productos):
    """
    Controls the flow of creating a new order.
    Parameters:
        pedidos (dict): current orders
        clientes (dict): registered clients
        productos (dict): registered products
    Returns:
        dict: updated orders dictionary 
    """
    # 1. Get data from the interface (View)
    pedido_id, cliente_id, producto_id, cantidad = pedir_datos_pedido()
    
    # 2. Validation logic: Look for the product price
    # Products are stored in a dictionary where values are tuples (id, name, price) [cite: 63, 65]
    if producto_id in productos:
        producto_info = productos[producto_id]
        # The price is the third element of the tuple [cite: 65]
        precio_unitario = producto_info[2] 
        
        # 3. Call the model function to process the order [cite: 71]
        nuevo_pedido_dict = crear_pedido(pedidos, pedido_id, cliente_id, producto_id, cantidad, precio_unitario)
        
        # 4. Update the orders dictionary if valid [cite: 27]
        if nuevo_pedido_dict is not None:
            pedidos[pedido_id] = nuevo_pedido_dict
        
        # 5. Get and display the status message from the view
        mensaje = mostrar_resultado_pedido(nuevo_pedido_dict)
        print(mensaje)
    else:
        # Error handling if product ID is not found
        print("Error: The product does not exist in the catalog.")

    # Always return the updated data structure 
    return pedidos