import streamlit as st


def set_sidebar_button():
    if st.session_state.stage == 1:
        st.button(
            label=":green[Iniciar partida]",
            args=[2],
            disabled=(
                False
                if all(
                    [
                        st.session_state.model,
                        st.session_state.writer,
                        st.session_state.parameters,
                    ]
                )
                else True
            ),
        )
    elif st.session_state.stage == 2:
        st.button(label=":red[Stop]")
    elif st.session_state.stage == 3:
        st.button(label=":green[Reset]")


def set_sidebar():
    with st.sidebar:
        st.header("Configuración")
        st.selectbox(
            "Modelo",
            options=["n-gramas"],
            format_func=str.title,
            index=None,
            key="model",
            placeholder="Modelo a utilizar",
            help="Seleccioná el modelo generativo.",
            label_visibility="visible",
        )
        st.selectbox(
            "Escritor",
            options=["Cortázar"],
            index=None,
            key="writer",
            placeholder="Escritor inspirador",
            help="Seleccioná el escritor.",
            label_visibility="visible",
        )
        st.text("Parámetros del modelo")
        st.selectbox(
            "N-gramas",
            options=["3"],
            index=None,
            key="parameters",
            placeholder="N-gramas para el modelo",
            help="Seleccioná la cantidad de n-gramas que quieras utilizar.",
            label_visibility="visible",
        )
        set_sidebar_button()
