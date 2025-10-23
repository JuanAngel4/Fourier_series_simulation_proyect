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


import numpy as np

def Fourier_Series_Terms(func, T, N, M, x_range):
    """
    Calcula la serie de Fourier y devuelve los términos individuales.
    
    Parameters:
        func : función periódica
        T : periodo
        N : número de coeficientes
        M : resolución
        x_range : tupla (x_min, x_max)
    
    Returns:
        x : vector de puntos
        s_total : suma de todos los términos
        terms : lista de diccionarios con cada término {'tipo':'cos/sin','n':n,'coef':coef,'valor':array}
    """
    x = np.linspace(*x_range, M)
    s_total = np.zeros_like(x)
    terms = []

    # Calcular coeficiente a0
    a0 = (2/T) * np.trapz(func(x), x)
    s_total += a0/2
    terms.append({'tipo':'a0', 'n':0, 'coef': a0/2, 'valor': np.full_like(x, a0/2)})

    # Calcular coeficientes an y bn
    for n in range(1, N+1):
        an = (2/T) * np.trapz(func(x) * np.cos(2*np.pi*n*x/T), x)
        bn = (2/T) * np.trapz(func(x) * np.sin(2*np.pi*n*x/T), x)

        term_cos = an * np.cos(2*np.pi*n*x/T)
        term_sin = bn * np.sin(2*np.pi*n*x/T)

        s_total += term_cos + term_sin

        terms.append({'tipo':'cos', 'n': n, 'coef': an, 'valor': term_cos})
        terms.append({'tipo':'sin', 'n': n, 'coef': bn, 'valor': term_sin})

    return x, s_total, terms
