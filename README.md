# Fourier Series Simulator | Digital Signal Processing | Numerical Approximation of Fourier Series
Check out the project here(just wait a few seconds!): https://fourier-series-simulation.streamlit.app
<img width="1024" height="1000" alt="url_qrcodecreator com_23_27_23" src="https://github.com/user-attachments/assets/ab84490c-c4b0-4403-9181-1bc2732ccf73" />

## 1. Overview

The **Fourier Series Simulator** is an interactive web application designed to visualize the Fourier decomposition of periodic functions.  
It provides a computational and graphical tool for students, researchers, and instructors working in:

- Mathematical Methods for Physics  
- Signal Processing  
- Harmonic Analysis  
- Applied Mathematics  
- Engineering Physics  

The application allows users to modify physical and numerical parameters in real time, observe the behavior of the Fourier approximation, and analyze the individual harmonic components that form the reconstruction of a periodic signal.

This project was developed by **Juan Ángel Gamez Díaz** as part of the course *Mathematical Methods for Physicists*.

---

## 2. Features

### 2.1 Interactive Visualization
- Real-time plot of the original periodic function.
- Fourier reconstructed signal for a finite number of terms.
- Option to display the individual sine and cosine components.
- Configurable domain and range for detailed inspection.

### 2.2 Customizable Parameters
- Choice of base periodic function (from a predefined catalog).
- Adjustable period \(T\).
- Adjustable number of Fourier coefficients \(N\).
- Adjustable maximum coefficient range \(N_{\text{max}}\).
- Sampling resolution \(M\).
- Independent control of \(x\)-axis and \(y\)-axis ranges.

### 2.3 LaTeX Fourier Series Output
- Full representation of the truncated Fourier series using LaTeX.
- Two-column aligned layout for improved readability.
- Rounded coefficients for clarity.

### 2.4 Suggestion System
- Users can propose new periodic functions.
- Suggestions stored in a local SQLite database with timestamps.

---

## 3. Mathematical Background

A piecewise continuous function \( f(x) \) periodic of period \( T \) can be represented by a Fourier series:

$$
f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\left(\frac{2\pi n}{T} x\right) + b_n \sin\left(\frac{2\pi n}{T} x\right) \right].
$$

The coefficients are computed as:

$$
a_n = \frac{2}{T}\int_{-T/2}^{T/2} f(x)\cos\left(\frac{2\pi n}{T} x\right)\, dx,
$$

$$
b_n = \frac{2}{T}\int_{-T/2}^{T/2} f(x)\sin\left(\frac{2\pi n}{T} x\right)\, dx.
$$

The simulator uses trapezoidal numerical integration over a grid of \(M\) points. The truncated Fourier series is:

$$
S_N(x) = \frac{a_0}{2} + \sum_{n=1}^{N} \left[ a_n\cos\left(\frac{2\pi n}{T}x\right) + b_n\sin\left(\frac{2\pi n}{T}x\right) \right].
$$

---

## 4. Installation

### 4.1 Requirements
- Python 3.10 or newer  
- Libraries:
  - `streamlit`
  - `numpy`
  - `matplotlib`
  - `sympy`
  - `sqlite3` (included with Python)

### 4.2 Setup

Clone the repository:

```bash
git clone https://github.com/your-username/fourier-series-simulator.git
cd fourier-series-simulator
