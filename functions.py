import numpy as np

# === FUNCIONES PERIÓDICAS CON PERIODO GENERAL T ===

def square_wave(x, T=2*np.pi):
    """Onda cuadrada periódica con periodo T."""
    x_mod = np.mod(x, T)
    return np.where(x_mod < T/2, 1, -1)


def triangular_wave(x, T=2*np.pi):
    """Onda triangular periódica con periodo T."""
    x_mod = np.mod(x, T)
    return 4 * np.abs(x_mod / T - np.floor(x_mod / T + 0.5)) - 1


def sawtooth_wave(x, T=2*np.pi):
    """Onda diente de sierra periódica con periodo T."""
    x_mod = np.mod(x, T)
    return 2 * (x_mod / T - np.floor(x_mod / T + 0.5))


def shifted_step(x, T=2*np.pi):
    """Onda escalón desplazada, con periodo T."""
    x_mod = np.mod(x, T)
    return np.where(x_mod < T/2, 1, 0)


def smooth_sine(x, T=2*np.pi):
    """Seno suavizado con armónico."""
    ω = 2 * np.pi / T
    return np.sin(ω * x) + 0.3 * np.sin(3 * ω * x)


def pulse_wave(x, T=2*np.pi, duty=0.3):
    """Onda de pulsos con ciclo útil 'duty' (0 < duty < 1)."""
    x_mod = np.mod(x, T)
    return np.where(x_mod < T * duty, 1, 0)


def half_rectified_sine(x, T=2*np.pi):
    """Seno rectificado de media onda."""
    ω = 2 * np.pi / T
    return np.maximum(0, np.sin(ω * x))


def full_rectified_sine(x, T=2*np.pi):
    """Seno rectificado de onda completa."""
    ω = 2 * np.pi / T
    return np.abs(np.sin(ω * x))


def multi_sine(x, T=2*np.pi):
    """Suma de varios armónicos con periodo base T."""
    ω = 2 * np.pi / T
    return np.sin(ω * x) + 0.5 * np.sin(3 * ω * x) + 0.25 * np.sin(5 * ω * x)


def amplitude_modulated(x, T=2*np.pi, m=0.5):
    """Seno modulado en amplitud."""
    ω = 2 * np.pi / T
    return (1 + m * np.sin(0.5 * ω * x)) * np.sin(ω * x)


def ripple_wave(x, T=2*np.pi):
    """Seno con ondulación de alta frecuencia."""
    ω = 2 * np.pi / T
    return np.sin(ω * x) + 0.1 * np.sin(10 * ω * x)


def clipped_sine(x, T=2*np.pi):
    """Seno recortado artificialmente."""
    ω = 2 * np.pi / T
    y = np.sin(ω * x)
    return np.clip(y, -0.5, 0.5)


# === DICCIONARIO DE FUNCIONES DISPONIBLES ===
waves = {
    "Square Wave": square_wave,
    "Triangular Wave": triangular_wave,
    "Sawtooth Wave": sawtooth_wave,
    "Shifted Step": shifted_step,
    "Smooth Sine": smooth_sine,
    "Pulse Wave": pulse_wave,
    "Half-Rectified Sine": half_rectified_sine,
    "Full-Rectified Sine": full_rectified_sine,
    "Multi-Sine": multi_sine,
    "Amplitude Modulated": amplitude_modulated,
    "Ripple Wave": ripple_wave,
    "Clipped Sine": clipped_sine
}
