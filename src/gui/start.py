import tkinter as tk
from tkinter import ttk
import os
import sys
from Utils import Meta_to_str as MtS
sys.path.append('src/code')  # Agrega la carpeta padre al path

from recomendations import recomend # Importa la función específica desde el archivo padre
from epub import extract_metadata

# Obtener la lista de archivos en la carpeta
archivos = os.listdir('data')

# Filtrar los archivos que terminan con .epub
archivos_epub = [archivo for archivo in archivos if archivo.endswith('.epub')]

for i in range (0, len(archivos_epub)):
    archivos_epub[i] = f'data/{archivos_epub[i]}'

meta = extract_metadata(archivos_epub, ['title', 'creator', 'genres'])

meta_info = []
for m in meta:
    a = f'{meta[m]}'
    meta_info.append(a[1:-1])

print(meta_info)

def mostrar_seleccion():
    seleccion = []
    for i, var in enumerate(vars):
        if var.get() == 1:
            seleccion.append(archivos_epub[i])
    
    if len(seleccion) == 0 :
        abrir_ventana_emergente("Lee un poco y culturizate sobrino")
        return
    
    if len(seleccion) == len(archivos_epub):
        abrir_ventana_emergente("Que mas quieres que te recomiende si ya lo leiste todo?")
        return
    
    recomended = recomend(seleccion)
    for wid in ventana.winfo_children():
        wid.destroy()

    new_label = tk.Label(ventana, text="Te recomiendo estos libros", font=("Arial", 20, "bold"), bg=color_crema)
    new_label.pack(side=tk.TOP, fill=tk.X)

    new_canvas = tk.Canvas(ventana, bg= color_crema)
    new_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear un widget Text dentro del Canvas
    text_widget = tk.Text(new_canvas, bg=color_crema)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Crear un widget Scrollbar y asociarlo con el Text
    new_scrollbar = tk.Scrollbar(new_canvas, command=text_widget.yview)
    new_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configurar el Text para usar la Scrollbar
    text_widget.config(yscrollcommand=new_scrollbar.set)

    # Insertar texto de ejemplo en el Text
    n = 1
    for r in MtS(recomended):
        text_widget.insert(tk.END, f" {n} -> {r}\n")
        n+=1



def abrir_ventana_emergente(msg):
    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Warning!!!")

    # Contenido de la ventana emergente
    label = tk.Label(ventana_emergente, text=msg)
    label.pack(padx=20, pady=20)

    # Hacer la ventana emergente modal
    ventana_emergente.grab_set()
    ventana.wait_window(ventana_emergente)

# Crear una instancia de la clase Tk, que representa la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Recomendador de libros")
color_crema = "#FFF8E7"
ventana.configure(bg=color_crema)

ventana.geometry("1240x720")

label = tk.Label(ventana, text="Que libros has leido?", font=("Arial", 20, "bold"), bg=color_crema)
label.pack(side=tk.TOP, fill=tk.X)

# Crear un Canvas para contener los Checkbuttons con Scrollbar
canvas = tk.Canvas(ventana, bg=color_crema)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Añadir un Scrollbar para controlar el desplazamiento del Canvas
scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Enlazar el Scrollbar con el Canvas
canvas.configure(yscrollcommand=scrollbar.set)

# Crear un Frame dentro del Canvas para contener los Checkbuttons
frame = tk.Frame(canvas, bg=color_crema)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Definir opciones
opciones = MtS(meta)    #archivos_epub #["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

# Crear variables para controlar el estado de los Checkbuttons
vars = []
for _ in opciones:
    var = tk.IntVar()
    vars.append(var)

# Crear Checkbuttons para cada opción dentro del Frame
for i, opcion in enumerate(opciones):
    checkbox = tk.Checkbutton(frame, text=opcion, bg=color_crema, variable=vars[i])
    checkbox.pack(anchor=tk.W)

# Configurar el tamaño del Canvas y el Frame
frame.update_idletasks()  # Actualizar el Frame para obtener su tamaño
canvas.config(scrollregion=canvas.bbox("all"))  # Configurar el tamaño del Canvas

# Botón para mostrar selección
boton_siguiente = tk.Button(ventana, text="Siguiente", command=mostrar_seleccion)
boton_siguiente.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
