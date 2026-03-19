# Function that calculates the total and creates the order dictionary
def crear_pedido(pedidos, pedido_id, cliente_id, producto_id, cantidad, precio_unitario):
    """
    Calculates total and formats the order as a dictionary.
    Returns:
        dict: The individual order or None if ID exists.
    """
    if pedido_id in pedidos:
        return None
    
    # Calculate total: total = unit_price * quantity [cite: 71, 72]
    total_pedido = precio_unitario * cantidad
    
    # Create the dictionary structure [cite: 56]
    nuevo_pedido = {
        "cliente": cliente_id,
        "producto": producto_id,
        "cantidad": cantidad,
        "total": total_pedido
    }
    return nuevo_pedido