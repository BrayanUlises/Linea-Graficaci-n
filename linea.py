import tkinter as tk
from tkinter import Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Inicializar variables
X1 = 20
X2 = 60
Y1 = 20
Y2 = 50

# Función para calcular la pendiente y mostrar la gráfica
def calcular_mostrar():
    # Obtener valores de las entradas
    global X1, X2, Y1, Y2
    X1 = float(entry_x1.get())
    X2 = float(entry_x2.get())
    Y1 = float(entry_y1.get())
    Y2 = float(entry_y2.get())

    # Calcular la pendiente
    M = round((Y2 - Y1) / (X2 - X1), 2)
    label_resultado.config(text=f"Pendiente de la recta: {M}")

    # Algoritmo DDA
    DX = abs(X1 - X2)
    DY = abs(Y1 - Y2)
    Numero_De_Pasos = int(max(DX, DY))
    Incremento_En_X = DX / Numero_De_Pasos
    Incremento_En_Y = DY / Numero_De_Pasos

    X = float(X1)
    Y = float(Y1)

    # Ajustar el incremento según el signo de la pendiente
    Incremento_En_X *= 1 if X2 >= X1 else -1
    Incremento_En_Y *= 1 if Y2 >= Y1 else -1

    Coordenadas_En_X = []
    Coordenadas_En_Y = []

    for i in range(Numero_De_Pasos):
        Coordenadas_En_X.append(round(X, 2))
        Coordenadas_En_Y.append(round(Y, 2))
        X = X + Incremento_En_X
        Y = Y + Incremento_En_Y

    # Tabla de valores obtenidos
    tabla_resultado.delete(1.0, tk.END)
    tabla_resultado.insert(tk.END, "X\tY\n")
    for i in range(Numero_De_Pasos):
        tabla_resultado.insert(tk.END, f"{Coordenadas_En_X[i]}\t{Coordenadas_En_Y[i]}\n")

    # Determinar dirección de la pendiente
    direccion = determinar_direccion(M)
    label_direccion.config(text=f"Dirección de la pendiente: {direccion}")

    # Gráfica resultante
    ax.clear()
    ax.plot(Coordenadas_En_X, Coordenadas_En_Y, linestyle='-', color="blue", marker="o", markersize=5, markerfacecolor="red")
    canvas.draw()

# Función para determinar la dirección de la pendiente
def determinar_direccion(pendiente):
    if pendiente > 1:
        return "Positiva (>1)"
    elif 0 < pendiente <= 1:
        return "Positiva (<=1)"
    elif -1 <= pendiente <= 0:
        return "Negativa (<=1)"
    else:
        return "Negativa (>1)"

# Función para limpiar las entradas y resultados
def limpiar_datos():
    entry_x1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_y1.delete(0, tk.END)
    entry_y2.delete(0, tk.END)
    label_resultado.config(text="Pendiente de la recta:")
    label_direccion.config(text="Dirección de la pendiente:")
    tabla_resultado.delete(1.0, tk.END)
    ax.clear()
    canvas.draw()

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Pendiente y Gráfica")

# Crear widgets
label_x1 = tk.Label(root, text="X1:")
entry_x1 = tk.Entry(root)
label_x2 = tk.Label(root, text="X2:")
entry_x2 = tk.Entry(root)
label_y1 = tk.Label(root, text="Y1:")
entry_y1 = tk.Entry(root)
label_y2 = tk.Label(root, text="Y2:")
entry_y2 = tk.Entry(root)

button_mostrar = tk.Button(root, text="Mostrar", command=calcular_mostrar)
button_limpiar = tk.Button(root, text="Limpiar Datos", command=limpiar_datos)

label_resultado = tk.Label(root, text="Pendiente de la recta:")
label_direccion = tk.Label(root, text="Dirección de la pendiente:")

tabla_resultado = Text(root, height=10, width=20)

# Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Organizar widgets en la interfaz
label_x1.grid(row=0, column=0)
entry_x1.grid(row=0, column=1)
label_x2.grid(row=1, column=0)
entry_x2.grid(row=1, column=1)
label_y1.grid(row=2, column=0)
entry_y1.grid(row=2, column=1)
label_y2.grid(row=3, column=0)
entry_y2.grid(row=3, column=1)

button_mostrar.grid(row=4, column=0, columnspan=2, pady=10)
button_limpiar.grid(row=5, column=0, columnspan=2, pady=10)
label_resultado.grid(row=6, column=0, columnspan=2)
label_direccion.grid(row=7, column=0, columnspan=2)
tabla_resultado.grid(row=8, column=0, columnspan=2)

canvas_widget.grid(row=0, column=2, rowspan=9)

# Establecer valores iniciales
entry_x1.insert(0, str(X1))
entry_x2.insert(0, str(X2))
entry_y1.insert(0, str(Y1))
entry_y2.insert(0, str(Y2))

# Ejecutar la interfaz
root.mainloop()
