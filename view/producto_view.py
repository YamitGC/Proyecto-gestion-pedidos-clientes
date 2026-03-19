# Function that requests product data from the user
def pedir_datos_producto():
    """
    Requests product data from the user.
    Returns:
        tuple: product_id, nombre_producto, precio_unidad
    """
    producto_id = input("Escribe el ID del producto: ")
    nombre_producto = input("Escribe el nombre del producto: ")
    precio_unidad = float(input("Escribe el precio: "))
    return producto_id, nombre_producto, precio_unidad

# Function that shows the result to the user
def mostrar_resultado(resultado):
    """
    Shows the result of the registration to the user.
    Parameters:
        resultado: result of the registration
    Returns:
        None
    """
    if resultado is None:
        print("Este producto ya existe")
    else:
        print("Producto registrado exitosamente")