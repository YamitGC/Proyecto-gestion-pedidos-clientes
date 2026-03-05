from app.colores import ROJO, VERDE, AMARILLO, CYAN, NEGRITA
def auth():
    print(CYAN + NEGRITA + "\n=== AUTENTICACIÓN ===")

    PIN_CORRECTO = "1234"
    intentos_maximos = 3

    for intento in range(intentos_maximos):
        pin = input(AMARILLO + "Ingrese su PIN: ")

        if pin == PIN_CORRECTO:
            print(VERDE + "Acceso concedido ✅")
            return True
        else:
            print(ROJO + f"PIN incorrecto ❌ Intentos restantes: {intentos_maximos - intento - 1}")

    print(ROJO + NEGRITA + "Tarjeta bloqueada 🚫")
    return False