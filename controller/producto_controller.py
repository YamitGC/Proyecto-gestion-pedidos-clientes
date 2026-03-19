from models.producto_model import productos, registrar_producto
from view.producto_view import pedir_datos_producto, mostrar_resultado

# Function that controls the product registration flow
def controlador_producto():
    """
    Controls the product registration flow.
    Returns:
        dict: updated products dictionary
    """
    producto_id, nombre_producto, precio_unidad = pedir_datos_producto()
    resultado = registrar_producto(productos, producto_id, nombre_producto, precio_unidad)
    mostrar_resultado(resultado)
    return productos