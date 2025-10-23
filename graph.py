import matplotlib.pyplot as plt

def plot_fourier(x, original, approx, N, label_func="Función"):
    plt.figure(figsize=(8, 4))
    plt.plot(x, original, label=label_func)
    plt.plot(x, approx, '--', label=f'Serie de Fourier (N={N})')
    plt.title("Aproximación de la Serie de Fourier")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
import matplotlib.pyplot as plt
import numpy as np

def plot_fourier2(x, original, approx, N, T, x_range, y_range, label_func):
    plt.figure(figsize=(9, 5))
    plt.plot(x, original, label=f"{label_func} (Original)", linewidth=1.8)
    plt.plot(x, approx, '--', label=f"Fourier Series (N={N})", linewidth=1.2)
    
    # === Configuración general ===
    plt.title("Aproximación de la Serie de Fourier", fontsize=13, fontweight='bold')
    plt.xlabel("x", fontsize=11)
    plt.ylabel("f(x)", fontsize=11)
    plt.grid(True, alpha=0.2)
    plt.legend()
    
    # === Límites ===
    plt.xlim(x_range)
    if y_range:
        plt.ylim(y_range)
    
    # === Mostrar texto con parámetros seleccionados ===
    text_info = (
        f"Función: {label_func}\n"
        f"N = {N}\n"
        f"T = {T:.3f}\n"
        f"x ∈ [{x_range[0]}, {x_range[1]}]"
    )
    if y_range:
        text_info += f"\ny ∈ [{y_range[0]}, {y_range[1]}]"
    
    plt.text(
        0.98, 0.98, text_info,
        transform=plt.gca().transAxes,
        fontsize=10,
        va='top', ha='right',
        bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.4')
    )
    
    plt.tight_layout()
    plt.show()
