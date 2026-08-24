import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="Equação do 1º Grau - Tinker Bell",
    page_icon="🧚‍♀️",
    layout="centered"
)


# ============================================
# TEMA - TINKER BELL 🧚‍♀️🌿✨
# ============================================

st.markdown("""
<style>

    /* FUNDO DA PÁGINA */
    .stApp {
        background: linear-gradient(
            135deg,
            #e8f5df,
            #cde8c5,
            #f6f1d1
        );
        color: #29452c;
    }

    /* TÍTULO */
    h1 {
        color: #315c38 !important;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px #b8cfa8;
    }

    /* SUBTÍTULOS */
    h2, h3 {
        color: #527d4d !important;
        font-weight: bold;
    }

    /* TEXTOS */
    p, label {
        color: #35583a !important;
    }

    /* CAMPOS DE ENTRADA */
    div[data-baseweb="input"] {
        background-color: #f5faef !important;
        border: 2px solid #9cba82 !important;
        border-radius: 12px;
    }

    input {
        color: #315c38 !important;
    }

    /* BOTÃO */
    .stButton > button {
        background: linear-gradient(
            90deg,
            #78a96b,
            #b59b4a
        );
        color: white;
        border: 2px solid #d6c36a;
        border-radius: 14px;
        font-weight: bold;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(75, 100, 55, 0.25);
    }

    /* HOVER DO BOTÃO */
    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #9bc48b,
            #d4bd5d
        );
        transform: scale(1.03);
        box-shadow: 0px 5px 15px rgba(91, 112, 59, 0.35);
    }

    /* ALERTAS */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* LINHA DIVISÓRIA */
    hr {
        border-color: #b59b4a;
    }

    /* CAPTION */
    .stCaption {
        color: #527d4d !important;
        text-align: center;
        font-weight: bold;
    }

    /* RESULTADO */
    div[data-testid="stSuccess"] {
        background-color: #dcefd3;
        border: 2px solid #8eb67d;
        color: #315c38;
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================
# CAMINHO DA PASTA DO PROGRAMA
# ============================================

PASTA_APP = Path(__file__).parent


# ============================================
# CAMINHO DA LOGOMARCA
# ============================================

CAMINHO_LOGO = PASTA_APP / "Clara Lourenço.jpg"


# ============================================
# LOGOMARCA
# ============================================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "⚠️ A imagem Maryangela.jpg não foi encontrada."
    )


# ============================================
# TÍTULO
# ============================================

st.title("✨ Equação do 1º Grau")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")


# ============================================
# ENTRADA DOS VALORES
# ============================================

a = st.number_input(
    "🌿 Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "✨ Digite o valor de b",
    value=0,
    step=1
)


# ============================================
# BOTÃO CALCULAR
# ============================================

if st.button(
    "🧚‍♀️ Calcular",
    use_container_width=True
):

    # ========================================
    # VERIFICA O VALOR DE A
    # ========================================

    if a == 0:

        if b == 0:

            st.warning(
                "✨ A equação possui infinitas soluções."
            )

        else:

            st.error(
                "🌿 A equação não possui solução."
            )

    else:

        # ====================================
        # CALCULA A RAIZ
        # ====================================

        x_raiz = -b / a


        # ====================================
        # RESULTADO
        # ====================================

        st.subheader("✨ Resultado")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"🌟 x = {x_raiz:.2f}"
        )


        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================

        st.subheader("📐 Equação")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )


        # ====================================
        # MOSTRA O CÁLCULO
        # ====================================

        st.subheader("📝 Resolução")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.latex(
            f"{a}x = {-b}"
        )

        st.latex(
            f"x = \\frac{{{-b}}}{{{a}}}"
        )

        st.latex(
            f"x = {x_raiz:.2f}"
        )


        # ====================================
        # GRÁFICO
        # ====================================

        st.subheader("📊 Gráfico da função")

        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        y = a * x + b


        # ====================================
        # CRIA GRÁFICO
        # ====================================

        fig, ax = plt.subplots(
            figsize=(8, 5)
        )


        # ====================================
        # DESENHA A RETA
        # ====================================

        ax.plot(
            x,
            y,
            color="#6f9f63",
            linewidth=2.5,
            label=f"y = {a}x + {b}"
        )


        # ====================================
        # EIXO X
        # ====================================

        ax.axhline(
            y=0,
            color="#b59b4a",
            linewidth=1.5
        )


        # ====================================
        # EIXO Y
        # ====================================

        ax.axvline(
            x=0,
            color="#b59b4a",
            linewidth=1.5
        )


        # ====================================
        # MARCA A RAIZ
        # ====================================

        ax.scatter(
            [x_raiz],
            [0],
            color="#d0b94f",
            s=120,
            zorder=5,
            label=f"Raiz x = {x_raiz:.2f}"
        )


        # ====================================
        # CONFIGURAÇÃO DO GRÁFICO
        # ====================================

        ax.set_xlabel(
            "x",
            color="#315c38"
        )

        ax.set_ylabel(
            "y",
            color="#315c38"
        )

        ax.set_title(
            "🧚‍♀️ Gráfico da Função do 1º Grau",
            color="#527d4d"
        )

        ax.grid(
            True,
            alpha=0.25
        )

        ax.legend()


        # ====================================
        # MOSTRA GRÁFICO
        # ====================================

        st.pyplot(fig)

        plt.close(fig)


# ============================================
# RODAPÉ
# ============================================

st.divider()

st.caption(
    "🧚‍♀️✨ Calculadora de Equação do 1º Grau • Jardim Encantado 🌿"
)
