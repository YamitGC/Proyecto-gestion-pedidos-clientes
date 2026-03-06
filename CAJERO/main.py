# Importamos la base de datos
from database.users import cuentas

# Importamos las funciones de la lógica (ajusta los nombres a los tuyos)
from app.logica_atm import *
from app.menu import menu
from app.auth import auth

def iniciar_programa():
    print("=== BIENVENIDO AL CAJERO AUTOMÁTICO PYTHON ===")
    
    # 1. Ejemplo de Login usando la data importada
    usuario_autenticado = auth(cuentas) 
    
    if usuario_autenticado:
        # 2. Si el login es exitoso, entramos al menú
        menu(usuario_autenticado)
    else:
        print("Acceso denegado. Saliendo...")

if __name__ == "__main__":
    iniciar_programa()

