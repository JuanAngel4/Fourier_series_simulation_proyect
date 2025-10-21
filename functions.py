import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.integrate import quad

def square_wave(x):
    return np.where(x >= 0, 1, -1)
def triangular_wave(x):
    return 2 * np.abs((x / np.pi) % 2 - 1) - 1
def sawtooth_wave(x):
    return 2 * (x / np.pi - np.floor(x / np.pi + 0.5))
def shifted_step(x):
    return np.where((x % (2*np.pi)) < np.pi, 1, 0)
def smooth_sine(x):
    return np.sin(x) + 0.3 * np.sin(3*x)







    