import numpy as np
import matplotlib.pyplot as plt
import functions as f
import graph as g
import series_calc as sc

# --- Parámetros globales ---
N = 30          # Número de términos en la serie
M = 1000            # Resolución (puntos de muestreo)
   # Dominio sobre el que se evalúa la señal
num_periods = 3


# --- Selección de la función base ---
# Usa el diccionario 'waves' definido en functions.py
# Puedes cambiar el nombre de la clave para probar distintas señales.
selected_wave = "Triangular Wave"  # <--- cambia aquí la señal
signal_func = f.waves[selected_wave]

# --- Crear el dominio ---
T = 6* np.pi
x_range = (-10, 10)
x = np.linspace(*x_range, 1000)

# --- Calcular la Serie de Fourier ---
x, s = sc.Fourier_Series(signal_func, T, N, M, x_range)
# --- Graficar resultados ---
label = f"{selected_wave} (Función Original)"
g.plot_fourier(x, signal_func(x), s, N, label_func=label)
