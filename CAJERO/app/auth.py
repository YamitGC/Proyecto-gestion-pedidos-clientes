from app.colores import *

def auth(cuentas):
    print(VERDE + NEGRITA + "\n=== SISTEMA DE SEGURIDAD ===" + RESET)

    intentos_usuario = 3

    # --- BUCLE PARA EL NOMBRE DE USUARIO ---
    for i_u in range(intentos_usuario):
        usuario_input = input(VERDE + "\nIngrese su nombre de usuario: " + RESET)
        
        # .capitalize() ayuda a que "luis" sea igual a "Luis" en tu BD
        usuario = usuario_input.capitalize()

        if usuario in cuentas:
            # SI EL USUARIO EXISTE, PASAMOS AL PIN
            print(VERDE + f"Usuario '{usuario}' reconocido. Proceda al PIN." + RESET)
            
            intentos_pin = 3
            pin_db = cuentas[usuario]["pin"]

            # --- BUCLE PARA EL PIN ---
            for i_p in range(intentos_pin):
                pin_ingresado = input(AMARILLO + f"Ingrese PIN para {usuario}: " + RESET)

                if pin_ingresado == pin_db:
                    print(VERDE + NEGRITA + "Acceso concedido ✅" + RESET)
                    return usuario  # Éxito total: devolvemos el nombre
                else:
                    restantes_p = intentos_pin - (i_p + 1)
                    if restantes_p > 0:
                        print(ROJO + f"PIN incorrecto ❌ Quedan {restantes_p} intentos." + RESET)

            # Si sale del bucle de PIN sin éxito
            print(ROJO + NEGRITA + f"\nPIN bloqueado 🚫 La cuenta de {usuario} ha sido restringida." + RESET)
            return None 

        else:
            # SI EL USUARIO NO EXISTE
            restantes_u = intentos_usuario - (i_u + 1)
            if restantes_u > 0:
                print(ROJO + f"Usuario no encontrado ❌ Intentos de búsqueda restantes: {restantes_u}" + RESET)
            else:
                print(ROJO + NEGRITA + "\nDemasiados intentos fallidos de usuario. Sistema bloqueado 🚫" + RESET)
                return None

    return None