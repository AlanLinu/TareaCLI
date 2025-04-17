import json
import os

ARCHIVO_TAREAS = "tareas.json" # Nombre del archivo donde guardaremos

def cargar_tareas():
    #Carga las tareas desde el archivo JSON.
    if not os.path.exists(ARCHIVO_TAREAS):
        return [] # Si no existe el archivo, devuelve lista vacía
    try:
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
            tareas = json.load(f)
        return tareas
    except (json.JSONDecodeError, FileNotFoundError):
        # Si hay error al leer o el archivo está vacío/corrupto
        return []

def guardar_tareas(tareas):
    #Guarda la lista de tareas (diccionarios) en el archivo JSON.
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
        # indent=4 hace que el JSON sea legible
        json.dump(tareas, f, indent=4, ensure_ascii=False)

def obtener_siguiente_id(tareas):
    if not tareas:
        return 1
    # Encuentra el ID más alto y suma 1
    max_id = max(tarea.get('id', 0) for tarea in tareas)
    return max_id + 1

def agregar_tarea(titulo, descripcion, fecha_limite):
    tareas = cargar_tareas()
    nuevo_id = obtener_siguiente_id(tareas)
    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "completada": False 
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"Tarea '{titulo}' agregada con ID {nuevo_id}.") 

def listar_tareas_formato():

    return cargar_tareas()

def marcar_como_completada(id_tarea):
    #Busca una tarea por ID y marca su estado como completada.
    tareas = cargar_tareas()
    tarea_encontrada = False
    for tarea in tareas:
        if tarea.get('id') == id_tarea:
            tarea['completada'] = True
            tarea_encontrada = True
            break 

    if tarea_encontrada:
        guardar_tareas(tareas)
        return True 
    else:
        return False