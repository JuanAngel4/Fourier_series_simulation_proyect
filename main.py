
# Importar módulos personalizados
import functions as f     # funciones base: señales (onda cuadrada, triangular, etc.)
import graph as g         # funciones gráficas (plot, estilos, etc.)
import series_calc as sc  # cálculos de coeficientes y serie de Fourier

# --- Parámetros de la simulación ---
T = 3.1416   # periodo
N = 10          # número de términos de la serie
M = 1000        # número de puntos para la simulación

# --- Selección de la función base ---
signal = f.sawtooth_wave  # puedes cambiarla por f.square_wave o f.sawtooth_wave

# --- Calcular Serie de Fourier ---
x, s = sc.Fourier_Series(signal, T, N, M)

# --- Graficar resultados ---
g.plot_fourier(x, signal(x), s, N, label_func="Función original")
