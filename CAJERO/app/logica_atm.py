from database.users import cuentas
from app.colores import *

def registrar_movimiento(usuario, tipo, monto):
    # Solo guardamos el texto del movimiento
    movimiento = f"{tipo}: ${monto:.2f}"
    # Buscamos la lista 'historial' dentro del diccionario del usuario
    cuentas[usuario]["historial"].append(movimiento)

def consultar_historial(usuario):
    print(f"\n--- HISTORIAL DE MOVIMIENTOS ---")
    print(f"Usuario: {usuario.upper()}")
    
    movimientos = cuentas[usuario].get("historial", [])
    
    if not movimientos:
        print("No hay movimientos registrados aún.")
    else:
        for i, m in enumerate(movimientos, 1):
            print(f"{i}. {m}")

def consultar_saldo(usuario):
    # Accedemos a la base de datos para obtener el saldo actual
    # Usamos .get() por seguridad, aunque ya sabemos que el usuario existe por el auth
    saldo = cuentas[usuario]["saldo"]
    
    print("\n" + "="*30)
    print(f"       ESTADO DE CUENTA")
    print("="*30)
    print(f"Cliente: {usuario.upper()}")
    print("Saldo disponible:" + VERDE + f" ${saldo:.2f}" + RESET)
    print("="*30)

def depositar_dinero(usuario):
    try:
        print(f"\n--- DEPÓSITO ---")
        monto = float(input("¿Cuánto deseas depositar?: "))

        
        if monto <= 5:
            print("Error: El monto debe ser mayor a $5")
        
    
        elif monto > 10000:
            print("Error: Por seguridad, no puedes depositar más de $10,000 por transacción.")
        
        else:
            # Si pasa las pruebas, procedemos
            cuentas[usuario]["saldo"] += monto
            registrar_movimiento(usuario, "DEPÓSITO", monto)
            
            print(f"✅ ¡Depósito exitoso!")
            print("Nuevo saldo:" + VERDE + f" ${cuentas[usuario]['saldo']:.2f}" + RESET)

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa solo números (ej: 100.50).")

def retirar_dinero(usuario):
    try:
        monto = float(input("¿Cuánto deseas retirar? (Mínimo $5): "))
        saldo_actual = cuentas[usuario]["saldo"]
        
        if 5 <= monto <= saldo_actual:
            cuentas[usuario]["saldo"] -= monto
            # REGISTRO EN EL HISTORIAL
            registrar_movimiento(usuario, "RETIRO", monto)
            print(f"Retiro exitoso. Saldo restante:" + ROJO + f" ${cuentas[usuario]['saldo']:.2f}" + RESET)
        
        elif monto < 5:
            # Mensaje específico para el límite mínimo
            print(f"Error: El monto mínimo de retiro es de {ROJO}$5.00{RESET}.")
            
        elif monto > saldo_actual:
            print("Error: Fondos insuficientes.")
            
    except ValueError:
        print("Error: Entrada inválida. Por favor ingresa un número.")