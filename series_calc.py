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
        #print(f"n={n}, a_n={an}, b_n={bn}")

    return x, s


import numpy as np


def Fourier_Series_Terms(func, T, N, M, x_range, tol=0.01, sig=3):
    """
    Calcula la serie de Fourier y devuelve los términos individuales de forma optimizada.
    Los coeficientes menores a 'tol' se consideran cero y no se agregan a la lista de términos.
    Todos los coeficientes se redondean a 'sig' cifras significativas.
    
    Parameters:
        func : función periódica
        T : periodo
        N : número de coeficientes
        M : resolución
        x_range : tupla (x_min, x_max)
        tol : tolerancia para coeficientes pequeños (default 0.01)
        sig : número de cifras significativas a mostrar (default 3)
    
    Returns:
        x : vector de puntos
        s_total : suma de todos los términos
        terms : lista de diccionarios con cada término {'tipo':'cos/sin','n':n,'coef':coef,'valor':array}
    """
    x = np.linspace(*x_range, M)
    y = func(x)
    s_total = np.zeros_like(x)
    terms = []

    # Coeficiente a0
    a0 = (2/T) * np.trapezoid(y, x)
    a0_disp = np.round(a0/2, sig)
    if abs(a0_disp) >= tol:
        s_total += a0_disp
        terms.append({'tipo':'a0', 'n':0, 'coef': a0_disp, 'valor': np.full_like(x, a0_disp)})

    # Precalcular cos y sin
    n_array = np.arange(1, N+1).reshape(-1,1)
    cos_matrix = np.cos(2*np.pi*n_array*x/T)
    sin_matrix = np.sin(2*np.pi*n_array*x/T)
    coef = 2/T

    for idx, n in enumerate(range(1, N+1)):
        an = coef * np.trapezoid(y * cos_matrix[idx,:], x)
        bn = coef * np.trapezoid(y * sin_matrix[idx,:], x)

        an_disp = np.round(an, sig)
        bn_disp = np.round(bn, sig)

        # Solo agregar términos significativos
        if abs(an_disp) >= tol:
            term_cos = an_disp * cos_matrix[idx,:]
            s_total += term_cos
            terms.append({'tipo':'cos', 'n': n, 'coef': an_disp, 'valor': term_cos})

        if abs(bn_disp) >= tol:
            term_sin = bn_disp * sin_matrix[idx,:]
            s_total += term_sin
            terms.append({'tipo':'sin', 'n': n, 'coef': bn_disp, 'valor': term_sin})

    return x, s_total, terms
