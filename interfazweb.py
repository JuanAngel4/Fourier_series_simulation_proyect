# interface.py
import streamlit as st
import numpy as np
import functions as f
import series_calc as sc
import matplotlib.pyplot as plt

# === PAGE CONFIGURATION ===
st.set_page_config(
    page_title="Fourier Series Simulator",
    layout="wide",
    page_icon="📈",
)

# === CUSTOM STYLES ===
st.markdown("""
    <style>
    body {background-color: #F8FAFC;}
    .main {background-color: #ffffff;}
    h1, h2, h3 {color: #1E3A8A;}
    .stSlider label, .stSelectbox label {font-weight: bold;}
    div[data-testid="stSidebar"] {
        background-color: #F0F4F8;
        color: #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# === TITLE ===
st.title("🎨 Interactive Fourier Series Simulator")
st.markdown("Explore how different periodic functions are approximated using their Fourier series.")

# --- SIDEBAR ---
st.sidebar.header("⚙️ Simulation Parameters")

# Base function selection
wave_names = list(f.waves_dic.keys())
selected_name = st.sidebar.radio("Select a base function:", wave_names)

# Adjustable parameters
T = st.sidebar.slider("Period (T)", 0.5, 10.0, 3.14, step=0.1)
N_max = st.sidebar.slider("Maximum number of coefficients (N max)", 5, 100, 30)
M = st.sidebar.slider("Sampling resolution (M)", 100, 2000, 500, step=100)

# X and Y range
x_min, x_max = st.sidebar.slider("X range", -20.0, 20.0, (-10.0, 10.0))
y_min, y_max = st.sidebar.slider("Y range", -3.0, 3.0, (-1.5, 1.5))

# Dynamic N control (sidebar slider)
N = st.sidebar.slider("Active coefficients (N)", 1, N_max, 6)

# === MAIN SECTION ===
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Fourier Series Plot")

    # Function selection and evaluation
    selected_func = f.waves_dic[selected_name]
    func_with_T = lambda x: selected_func(x, T)

    x_range = (x_min, x_max)
    x = np.linspace(*x_range, M)
    y_original = func_with_T(x)

    # Fourier series calculation
    x, s = sc.Fourier_Series(func_with_T, T, N, M, x_range)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y_original, label=f"{selected_name} (Original)", linewidth=2, color="#1E40AF")
    ax.plot(x, s, '--', label=f"Fourier Series (N={N})", linewidth=1.5, color="#F97316")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(alpha=0.3)
    ax.legend()
    ax.set_title("Fourier Series Approximation", fontsize=13, fontweight='bold')
    st.pyplot(fig)

with col2:
    st.subheader("📋 Current Parameters")
    st.markdown(f"""
    **Selected function:** `{selected_name}`  
    **Period (T):** {T:.3f}  
    **Number of coefficients (N):** {N}  
    **Resolution (M):** {M}  
    **X domain:** [{x_min}, {x_max}]  
    **Y range:** [{y_min}, {y_max}]
    """)

st.markdown("---")
st.caption("Developed by Juan Ángel Gamez Diaz — Interactive Fourier Visualizer")
