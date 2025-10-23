import numpy as np
import matplotlib.pyplot as plt
import functions as f
import graph as g
import series_calc as sc

# --- Parámetros ---
N = 6
M = 200
T =  np.pi
x_range = (-10, 10)
x = np.linspace(*x_range, M)
selected_wave = 10  # 0 = square_wave, 1 = triangular_wave, etc.
# --- Selección de la función base ---
signal_func = f.waves_list()[selected_wave]
print(f"Función seleccionada: {signal_func.__name__}")

# --- Empaquetar función con su T ---
func_with_T = lambda x: signal_func(x, T)

# --- Calcular la Serie de Fourier ---
x, s = sc.Fourier_Series(func_with_T, T, N, M, x_range)
y_range = (-1.5, 1.5)
# --- Graficar resultados ---
label = signal_func.__name__
#g.plot_fourier(x, func_with_T(x), s, N, label_func=label)

g.plot_fourier2(x, func_with_T(x), s, N, T, x_range, y_range, label_func=label)
