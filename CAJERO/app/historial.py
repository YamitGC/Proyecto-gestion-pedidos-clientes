historial = []

def agregar_historial(operacion):
    historial.append(operacion) #añade la operacion al final de la lista

def mostrar_historial():
    if len(historial) == 0: #verifica si no hay operaciones registradas
        print("No hay operaciones registradas.")
        return
    for i, entrada in enumerate(historial, 1): #recorre la lista numerando desde 1
        print(f"{i}. {entrada}") # imprime cada operacion con su numero