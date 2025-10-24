import streamlit as st
st.set_page_config(
    page_title="Fourier Series Simulator",
    layout="wide",
    page_icon="📈",
     initial_sidebar_state="expanded"
)


import streamlit as st
import numpy as np
import functions as f
import series_calc as sc
import matplotlib.pyplot as plt

# === PAGE CONFIGURATION ===


# === CUSTOM STYLES ===
st.markdown("""
<style>
body {background-color: #F8FAFC;}
.main {background-color: #ffffff;}
h1, h2, h3 {color: #1E3A8A;}
.stSlider label, .stSelectbox label {font-weight: bold;}
div[data-testid="stSidebar"] {background-color: #F0F4F8;color: #1E3A8A;}
</style>
""", unsafe_allow_html=True)



# === TITLE ===
st.title("Interactive Fourier Series Simulator")
st.markdown("Explore how different periodic functions are approximated using their Fourier series.")


# --- SIDEBAR ---
st.sidebar.header("⚙️ Simulation Parameters")
wave_names = list(f.waves_dic.keys())
selected_name = st.sidebar.radio("Select a base function:", wave_names)

T = st.sidebar.slider("Period (T)", 0.5, 10.0, 3.14, step=0.1)
N_max = st.sidebar.slider("Maximum number of coefficients (N max)", 5, 100, 30)
N = st.sidebar.slider("Active coefficients (N)", 1, N_max, 6)
M = st.sidebar.slider("Sampling resolution (M)", 100, 2000, 500, step=100)
x_min, x_max = st.sidebar.slider("X range", -20.0, 20.0, (-10.0, 10.0),step=0.5)
y_min, y_max = st.sidebar.slider("Y range", -3.0, 3.0, (-1.5, 1.5),step=0.5)


# === MAIN SECTION ===
col1, col2 = st.columns([2,1])

# Función y rango
selected_func = f.waves_dic[selected_name]
func_with_T = lambda x: selected_func(x, T)
x_range = (x_min, x_max)
x = np.linspace(*x_range, M)
y_original = func_with_T(x)

# --- CÁLCULO DE LA SERIE EXACTA ---
x_s, s_total = sc.Fourier_Series(func_with_T, T, N, M, x_range)

# --- CÁLCULO DE LOS TÉRMINOS PARA VISUALIZACIÓN ---
x_terms, s_dummy, terms_list = sc.Fourier_Series_Terms(func_with_T, T, N, M, x_range)

# --- CONSTRUCCIÓN DE EXPRESIÓN REDONDEADA ---
# Construcción de expresión LaTeX de términos para mostrar
terms_latex = r"\begin{alignat*}{2}"  # El 2 indica dos columnas
col_count = 0

for t in terms_list:
    coef = round(t['coef'], 3)
    if t['tipo'] == 'a0':
        term_str = f"{coef}"
    elif t['tipo'] == 'cos':
        n_val = round(2*t['n']/T, 4)
        term_str = f"+ {coef} \\cos({n_val} \\pi x)"
    elif t['tipo'] == 'sin':
        n_val = round(2*t['n']/T, 4)
        term_str = f"+ {coef} \\sin({n_val} \\pi x)"
    
    # Agregar a la cadena según la columna
    if col_count % 2 == 0:  # primera columna
        terms_latex += term_str + " & "  # & separa columnas
    else:  # segunda columna
        terms_latex += term_str + r" \\ "  # \\ para nueva fila
    col_count += 1

# Si el número de términos es impar, agregar un salto de fila al final
if col_count % 2 != 0:
    terms_latex += r"\\"

terms_latex += r"\end{alignat*}"

st.markdown("<h3 style='text-align: center;'> Fourier Series Terms</h3>", unsafe_allow_html=True)
st.latex(terms_latex)



# === PLOT EN COL1 ===
# === CHECKBOXES DE VISUALIZACIÓN ===
show_terms = st.sidebar.checkbox("Show individual Fourier terms", value=True)
show_signals = st.sidebar.checkbox("Show original & Fourier sum", value=True)

# === PLOT EN COL1 ===
with col1:
    st.subheader("Fourier Series Plot with Individual Terms")
    fig, ax = plt.subplots(figsize=(12,6))
    
    # Señal original y Fourier sum
    if show_signals:
        ax.plot(x, y_original, label=f"{selected_name} (Original)", linewidth=2, color="#1F222F")
        ax.plot(x, s_total, '-.', color='orange', label='Fourier Sum', linewidth=2)
    
    # Términos individuales (fondo)
    if show_terms:
        term_color = '#B0C4DE'  # light steel blue
        for t in terms_list:
            if t['tipo'] != 'a0':
                ax.plot(x, t['valor'], '--', color=term_color, linewidth=1)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)
    st.pyplot(fig)

# === INFORMACIÓN Y PARÁMETROS EN COL2 ===
with col2:
    st.subheader("Current Parameters")
    st.markdown(f"""
    **Selected function:** `{selected_name}`  
    **Period (T):** {T:.3f}  
    **Number of coefficients (N):** {N}  
    **Resolution (M):** {M}  
    **X domain:** [{x_min}, {x_max}]  
    **Y range:** [{y_min}, {y_max}]
    """)

st.markdown("---")
st.caption("Developed by Juan Ángel Gamez Diaz — Interactive Fourier Visualizer | Mathematical Metods for phisicists Course Project")

# === SECCIÓN DE SUGERENCIAS AL FINAL ===
import sqlite3
from datetime import datetime

# === CONEXIÓN A BASE DE DATOS ===
# === SECCIÓN DE SUGERENCIAS AL FINAL ===
import sqlite3
from datetime import datetime

# === CONEXIÓN A BASE DE DATOS ===
conn = sqlite3.connect("suggestions.db")
cursor = conn.cursor()

# Crear tabla si no existe

conn.commit()

# === SECCIÓN DE INTERFAZ ===
with st.expander("💡 Is there any periodical function you want us to add?"):
    st.markdown("We’d love to hear your suggestions! Please describe the function below:")
    
    user_suggestion = st.text_area("✍️ Your suggestion:", placeholder="Describe the function or its formula...")
    
    if st.button("Send suggestion"):
        if user_suggestion.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 👉 AQUÍ SE GUARDA LA SUGERENCIA
            cursor.execute(
                "INSERT INTO suggestions (suggestion, timestamp) VALUES (?, ?)",
                (user_suggestion.strip(), timestamp)
            )
            conn.commit()
            
            st.success("✅ Thank you for your suggestion! We'll review it soon.")
        else:
            st.warning("⚠️ Please write something before sending.")

# Cerrar la conexión al final
conn.close()


