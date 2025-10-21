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
