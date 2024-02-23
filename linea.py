import tkinter as tk
from tkinter import Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Función para calcular la pendiente y mostrar la gráfica
def calcular_pendiente():
    X1 = float(entry_x1.get())
    X2 = float(entry_x2.get())
    Y1 = float(entry_y1.get())
    Y2 = float(entry_y2.get())

    M = (Y2 - Y1) / (X2 - X1)
    label_resultado.config(text=f"Pendiente de la recta: {M}")

    # Algoritmo DDA
    DX = abs(X1 - X2)
    DY = abs(Y1 - Y2)
    Numero_De_Pasos = int(max(DX, DY))
    Incremento_En_X = DX / Numero_De_Pasos
    Incremento_En_Y = DY / Numero_De_Pasos

    X = float(X1)
    Y = float(Y1)

    Coordenadas_En_X = []
    Coordenadas_En_Y = []

    for i in range(Numero_De_Pasos):
        Coordenadas_En_X.append(X)
        Coordenadas_En_Y.append(Y)
        X = X + Incremento_En_X
        Y = Y + Incremento_En_Y

    # Tabla de valores obtenidos
    tabla_resultado.delete(1.0, tk.END)
    tabla_resultado.insert(tk.END, "X\tY\n")
    for i in range(Numero_De_Pasos):
        tabla_resultado.insert(tk.END, f"{Coordenadas_En_X[i]}\t{Coordenadas_En_Y[i]}\n")

    # Gráfica resultante
    ax.clear()
    ax.plot(Coordenadas_En_X, Coordenadas_En_Y, linestyle='-', color="blue", marker="o", markersize=5, markerfacecolor="red")
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

button_calcular = tk.Button(root, text="Calcular Pendiente y Graficar", command=calcular_pendiente)
label_resultado = tk.Label(root, text="Pendiente de la recta: ")

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

button_calcular.grid(row=4, column=0, columnspan=2)
label_resultado.grid(row=5, column=0, columnspan=2)
tabla_resultado.grid(row=6, column=0, columnspan=2)

canvas_widget.grid(row=0, column=2, rowspan=7)

# Establecer los valores iniciales
entry_x1.insert(0, str(X1))
entry_x2.insert(0, str(X2))
entry_y1.insert(0, str(Y1))
entry_y2.insert(0, str(Y2))

# Ejecutar la interfaz
root.mainloop()
