import gestor_tareas
import datetime 

def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar nueva tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    print("-------------------------")

def solicitar_datos_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción: ")
    fecha_valida = False
    while not fecha_valida: 
        fecha_limite_str = input("Ingrese la fecha límite (formato AAAA-MM-DD): ")
        try:
            # Intenta convertir la cadena a fecha con el formato esperado
            datetime.datetime.strptime(fecha_limite_str, '%Y-%m-%d')
            fecha_valida = True 
        except ValueError:
            # Si strptime falla, lanza un ValueError
            print("Formato de fecha incorrecto. Por favor use AAAA-MM-DD.")
    return titulo, descripcion, fecha_limite_str

def mostrar_lista_tareas(tareas):
    if not tareas:
        print("No hay tareas guardadas.")
        return

    print("\n--- Lista de Tareas ---")
    for tarea in tareas:
        estado = "Completada" if tarea.get('completada', False) else "Pendiente"
        print(f"ID: {tarea.get('id', 'N/A')}")
        print(f"  Título: {tarea.get('titulo', 'Sin título')}")
        print(f"  Descripción: {tarea.get('descripcion', '')}")
        print(f"  Fecha Límite: {tarea.get('fecha_limite', 'N/A')}")
        print(f"  Estado: {estado}")
        print("-" * 10) 

def solicitar_id_completar():
    """Pide al usuario el ID de la tarea a completar."""
    while True:
        try:
            id_str = input("Ingrese el ID de la tarea a marcar como completada: ")
            id_tarea = int(id_str)
            return id_tarea
        except ValueError:
            print("Error: Por favor ingrese un número válido para el ID.")


if __name__ == "__main__": 
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agregar Tarea
            titulo, desc, fecha = solicitar_datos_tarea()
            gestor_tareas.agregar_tarea(titulo, desc, fecha)
        elif opcion == '2':
            # Listar Tareas
            tareas_cargadas = gestor_tareas.listar_tareas_formato()
            mostrar_lista_tareas(tareas_cargadas)
        elif opcion == '3':
            # Marcar como Completada
            tareas_cargadas = gestor_tareas.listar_tareas_formato() # Mostramos para que elija ID
            if tareas_cargadas: # Solo pedir ID si hay tareas
                 mostrar_lista_tareas(tareas_cargadas)
                 id_a_completar = solicitar_id_completar()
                 if gestor_tareas.marcar_como_completada(id_a_completar):
                     print(f"Tarea con ID {id_a_completar} marcada como completada.")
                 else:
                     print(f"Error: No se encontró una tarea con ID {id_a_completar}.")
            else:
                 print("No hay tareas para marcar como completadas.")
        elif opcion == '4':
            # Salir
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")