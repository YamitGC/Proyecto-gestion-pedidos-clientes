from app.clean_screen import clean_screen
from app.progress_bar import progress_bar
from app.logica_atm import *
from app.colores import *


historial = []

def agregar_historial(operacion):
    historial.append(operacion) #añade la operacion al final de la lista

def mostrar_historial():
    if len(historial) == 0: #verifica si no hay operaciones registradas
        print("No hay operaciones registradas.")
        return
    for i, entrada in enumerate(historial, 1): #recorre la lista numerando desde 1
        print(f"{i}. {entrada}") # imprime cada operacion con su numero


def menu(usuario):
    while True: # <--- Iniciamos el bucle infinito
        # Limpiamos la pantalla antes de mostrar el menú principal
        # clean_screen() 
        
        print("\n" + VERDE + "="*30 + RESET)
        print(f"  BIENVENIDO/A, {usuario.upper()}")
        print(VERDE + "="*30 + RESET)
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Historial")
        print("5. Salir del cajero")

        try:
            opcion = int(input("\nIngresa la opcion (1-5): "))
        except ValueError:
            print("Error: Por favor, ingresa solo números.")
            continue # Reinicia el bucle si no es un número

        if opcion == 1:
            clean_screen()
            progress_bar()
            consultar_saldo(usuario)
            input("\nPresiona ENTER para volver al menú...") 
        
        elif opcion == 2:
            clean_screen()
            progress_bar()
            depositar_dinero(usuario)
            input("\nPresiona ENTER para volver al menú...")
        
        elif opcion == 3:
            clean_screen()
            progress_bar()
            retirar_dinero(usuario)
            input("\nPresiona ENTER para volver al menú...")

        elif opcion == 4:
            clean_screen()
            progress_bar()
            consultar_historial(usuario)
            input("\nPresiona ENTER para volver al menú...")

        elif opcion == 5:
            print("Cerrando el cajero... ¡Vuelva pronto!")
            break

        else:
            print("Opcion incorrecta, digite una opcion valida (1-5).")
            input("\nPresiona ENTER para intentar de nuevo...")


