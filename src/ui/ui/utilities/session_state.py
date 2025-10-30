import streamlit as st


def change_turn(value: str):
    if "turn" in st.session_state:
        setattr(st.session_state, "turn", value)


def set_session_state_keys(*args, **kwargs):
    for key, value in kwargs.items():
        if key not in st.session_state:
            setattr(st.session_state, key, value)
