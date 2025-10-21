import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import functions as f
import series_calc as sc
import graph as g  # Si quieres, puedes usar tu función g.plot_fourier() para consistencia


class FourierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualizador de Series de Fourier")
        self.geometry("1000x700")
        self.configure(bg="#1e1e1e")

        # --- Variables controladas por interfaz ---
        self.selected_wave = tk.StringVar(value="Square Wave")
        self.T = tk.DoubleVar(value=2 * np.pi)
        self.N = tk.IntVar(value=10)
        self.M = tk.IntVar(value=1000)
        self.x_min = tk.DoubleVar(value=-8)
        self.x_max = tk.DoubleVar(value=8)

        # --- Configuración visual ---
        style = ttk.Style(self)
        style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=4)
        style.configure("TEntry", padding=2)

        # --- Estructura general ---
        self.create_widgets()
        self.create_plot_area()

    def create_widgets(self):
        # --- Panel lateral de controles ---
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        ttk.Label(control_frame, text="⚙️ Parámetros de la Serie de Fourier").pack(pady=5)

        # Parámetros numéricos
        self.add_param_entry(control_frame, "Periodo T:", self.T)
        self.add_param_entry(control_frame, "Términos N:", self.N)
        self.add_param_entry(control_frame, "Resolución M:", self.M)
        self.add_param_entry(control_frame, "x_min:", self.x_min)
        self.add_param_entry(control_frame, "x_max:", self.x_max)

        ttk.Separator(control_frame, orient='horizontal').pack(fill='x', pady=10)

        ttk.Label(control_frame, text="📈 Seleccionar Función:").pack(pady=5)

        # --- Botones de selección de función ---
        for name in f.waves.keys():
            ttk.Radiobutton(
                control_frame,
                text=name,
                variable=self.selected_wave,
                value=name
            ).pack(anchor='w')

        ttk.Separator(control_frame, orient='horizontal').pack(fill='x', pady=10)

        ttk.Button(control_frame, text="Graficar Serie de Fourier", command=self.plot_fourier).pack(pady=10)
        ttk.Button(control_frame, text="Salir", command=self.destroy).pack(pady=5)

    def add_param_entry(self, parent, label, var):
        frame = ttk.Frame(parent)
        frame.pack(fill='x', pady=3)
        ttk.Label(frame, text=label, width=15).pack(side=tk.LEFT)
        ttk.Entry(frame, textvariable=var, width=10).pack(side=tk.LEFT)

    def create_plot_area(self):
        # --- Área del gráfico ---
        self.fig, self.ax = plt.subplots(figsize=(6, 5), dpi=100)
        self.fig.patch.set_facecolor("#1e1e1e")
        self.ax.set_facecolor("#2d2d2d")
        self.ax.grid(True, color="gray", alpha=0.3)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def plot_fourier(self):
        try:
            # Obtener parámetros
            T = float(self.T.get())
            N = int(self.N.get())
            M = int(self.M.get())
            x_min, x_max = float(self.x_min.get()), float(self.x_max.get())
            func_name = self.selected_wave.get()
            func = f.waves[func_name]

            # Crear dominio
            x = np.linspace(x_min, x_max, M)

            # Calcular serie de Fourier
            x, s = sc.Fourier_Series(func, T, N, M, (x_min, x_max))

            # Limpiar y graficar
            self.ax.clear()
            self.ax.plot(x, func(x), label="Función original", color="#00ff99", linewidth=2)
            self.ax.plot(x, s, label=f"Serie de Fourier (N={N})", color="#ffcc00", linewidth=2)
            self.ax.set_title(f"{func_name}", color="white", fontsize=12)
            self.ax.legend(facecolor="#2d2d2d", edgecolor="gray", labelcolor="white")
            self.ax.grid(True, color="gray", alpha=0.4)
            self.ax.set_facecolor("#2d2d2d")

            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error al calcular o graficar:\n{e}")


if __name__ == "__main__":
    app = FourierApp()
    app.mainloop()
