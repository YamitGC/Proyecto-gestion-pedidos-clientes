from database.users import cuentas


def consultar_saldo(usuario):
    saldo = cuentas.get(usuario, 0)
    print(f"\n--- CONSULTA ---")
    print(f"Usuario: {usuario.upper()}")
    print(f"Tu saldo actual es: ${saldo:.2f}")

def depositar_dinero(usuario):
    try:
        monto = float(input("¿Cuánto deseas depositar?: "))
        if monto > 0:
            cuentas[usuario] += monto
            print(f"¡Depósito exitoso! Nuevo saldo: ${cuentas[usuario]:.2f}")
        else:
            print("Error: El monto debe ser mayor a 0.")
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa solo números.")

def retirar_dinero(usuario):
    try:
        monto = float(input("¿Cuánto deseas retirar?: "))
        if 0 < monto <= cuentas[usuario]:
            cuentas[usuario] -= monto
            print(f"Retiro exitoso. Saldo restante: ${cuentas[usuario]:.2f}")
        elif monto > cuentas[usuario]:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: El monto debe ser mayor a 0.")
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingresa solo números.")
