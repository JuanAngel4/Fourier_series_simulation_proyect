import numpy as np

def Coeff_a0(f,T,M):
    """Calcula el coeficiente a_0 de Fourier de una funcion dada."""
    a = -T/2
    b = T/2
    x = np.linspace(a,b,M)
    y = f(x)
    a0 = 2/T * np.trapezoid(y,x)
    return a0

def Coeffs_an_bn(f,T,n,M):
    """Calcula los coeficientes de Fourier a_n, b_n de una funcion dada."""
    a = -T/2
    b = T/2

    x = np.linspace(a,b,M)
    y1 = f(x)*(np.cos((2*n*np.pi*x)/T))
    y2 = f(x)*(np.sin((2*n*np.pi*x)/T))
    coef = 2/T  

    an = coef * np.trapezoid(y1,x)
    bn = coef * np.trapezoid(y2,x)

    return an, bn

def Fourier_Series(f, T, N, M, x_range):
    """Calcula la serie de Fourier hasta N términos."""
    a, b = x_range
    x = np.linspace(a, b, M)
    s = Coeff_a0(f, T,M) / 2

    for n in range(1, N + 1):
        an, bn = Coeffs_an_bn(f, T, n, M)
        s += an * np.cos(2 * n * np.pi * x / T) + bn * np.sin(2 * n * np.pi * x / T)
        print(f"n={n}, a_n={an}, b_n={bn}")

    return x, s