# Gestor de Tareas Simple en Consola

Una aplicación básica de línea de comandos (CLI) escrita en Python para administrar una lista personal de tareas. Permite agregar, listar y marcar tareas como completadas. Las tareas se guardan en un archivo `tareas.json`.

## Características Principales

* **Agregar Tareas:** Permite añadir nuevas tareas especificando título, descripción y fecha límite (formato AAAA-MM-DD).
* **Listar Tareas:** Muestra todas las tareas guardadas, indicando claramente su ID, detalles y estado (Pendiente o Completada).
* **Marcar como Completadas:** Permite cambiar el estado de una tarea de "Pendiente" a "Completada" usando su ID.
* **Almacenamiento Persistente:** Las tareas se guardan en el archivo `tareas.json` en la misma carpeta, para que no se pierdan al cerrar la aplicación.
* **Validación de Fecha:** Asegura que la fecha límite introducida por el usuario siga el formato `AAAA-MM-DD`.

## Prerrequisitos

* Tener **Python 3.x** instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

## Instalación / Configuración

No requiere una instalación compleja. Solo necesitas los archivos del proyecto:

1.  Descarga o clona los archivos `main.py` y `gestor_tareas.py`.
2.  Asegúrate de que ambos archivos estén en la misma carpeta.

## Instrucciones de Uso

**Paso 1: Encuentra la Carpeta del Programa**

* Primero, busca en tu computadora la carpeta donde guardaste los dos archivos del programa: `main.py` y `gestor_tareas.py`.
* Recuerda bien dónde está esa carpeta, la necesitarás en un momento.

**Paso 2: Abre la "Ventana de Comandos"**

* Necesitamos abrir una ventana donde le daremos instrucciones escritas a la computadora.
    * **En Windows:** Busca "Símbolo del sistema" (o "Command Prompt") o "PowerShell" en el menú de inicio y haz clic para abrirlo. Verás una ventana, usualmente negra o azul, donde puedes escribir.
    * **En Mac:** Ve a la carpeta "Aplicaciones", luego entra a la carpeta "Utilidades" y haz doble clic en "Terminal".
    * **En Linux:** Busca y abre una aplicación llamada "Terminal" (el icono suele ser una pantalla negra).

**Paso 3: Dile a la Ventana de Comandos Dónde Está tu Carpeta **

* Necesitamos que la ventana de comandos "mire" dentro de la carpeta donde están tus archivos `main.py` y `gestor_tareas.py`. Hay una forma fácil de intentarlo:
    1.  Ve a la carpeta donde guardaste los archivos `main.py` y `gestor_tareas.py` usando el explorador de archivos normal de tu computadora.
    2.  Haz clic con el **botón derecho del ratón** en un espacio vacío *dentro* de esa carpeta.
    3.  Busca en el menú que aparece una opción que diga algo como:
        * "Abrir en Terminal"
        * "Abrir ventana de comandos aquí"
        * "Abrir con PowerShell aquí"
        * "Open in Terminal" o similar.
    4.  Si encuentras una de esas opciones, ¡haz clic en ella! Se abrirá una nueva ventana de comandos ya lista en el lugar correcto. Si es así, puedes saltar al Paso 4.
* **Si *no* encontraste la opción "Abrir aquí":** lo haremos de otra forma.
    1.  Vuelve a la ventana de comandos que abriste en el Paso 2.
    2.  Escribe `cd ` (importante: escribe 'c', luego 'd', y luego **un espacio**). No presiones Enter todavía.
    3.  Ahora, necesitas la "dirección" de tu carpeta. Ve a la ventana del explorador de archivos donde está tu carpeta. Arriba, suele haber una barra que muestra dónde estás (ej. `C:\Usuarios\TuNombre\Documentos\ProyectoTareas`). Haz clic en esa barra para que se seleccione la dirección completa y cópiala (clic derecho -> Copiar, o Ctrl+C).
    4.  Regresa a la ventana de comandos. Después del `cd ` que escribiste, pega la dirección que copiaste (clic derecho -> Pegar, o Ctrl+V).
    5.  Ahora sí, presiona la tecla **Enter**. Esto le dice a la ventana de comandos que "entre" a tu carpeta.

**Paso 4: Inicia el Programa de Tareas**

* ¡Ya casi! Ahora que la ventana de comandos está en la carpeta correcta, escribe *exactamente* lo siguiente (respetando minúsculas y el espacio):
    ```
    python main.py
    ```
* Después de escribirlo, presiona la tecla **Enter**.

**Paso 5: Usa el Menú del Programa**

* Si todo salió bien, ¡verás el menú del programa de tareas en la ventana de comandos!
    ```
    --- Gestor de Tareas ---
    1. Agregar nueva tarea
    2. Listar todas las tareas
    3. Marcar tarea como completada
    4. Salir
    -------------------------
    Seleccione una opción:
    ```
* Ahora es fácil:
    * Para elegir qué quieres hacer, **escribe el número** de la opción (por ejemplo, `1` si quieres agregar una tarea).
    * Presiona la tecla **Enter**.
    * El programa te hará preguntas si necesita más información (como el título o la fecha). Escribe tu respuesta y presiona **Enter** cada vez.
    * Sigue las instrucciones que te da el programa.
    * Cuando quieras cerrar el programa, elige la **opción 4** y presiona **Enter**.

**Paso 6: ¿Dónde se Guardan las Tareas?**

* No tienes que preocuparte por guardar manualmente. Cada vez que agregas o marcas una tarea como completada, el programa guarda todo automáticamente en un archivo llamado `tareas.json`. Este archivo aparecerá en la misma carpeta donde tienes `main.py`.


## Capturas de Pantalla (Ejemplos)

**1. Menú Principal:**

![image](https://github.com/user-attachments/assets/2c741eed-d4e2-4d9d-bb7b-cbcab0eb7229)

**2. Agregando una Nueva Tarea:**

![image](https://github.com/user-attachments/assets/356b51cd-c692-483d-9fc2-236190c59738)

**3. Listando las Tareas Existentes:**

![image](https://github.com/user-attachments/assets/8fe6632e-3cf9-4bc0-8b14-3eb13511bf62)


**4. Marcando una Tarea como Completada:**

![image](https://github.com/user-attachments/assets/437d2dbd-09ce-41ff-b058-0c49ea322de5)
![image](https://github.com/user-attachments/assets/d99f204d-2244-4ef9-bd2b-3eaa8db36ca0)

