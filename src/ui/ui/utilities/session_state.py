import streamlit as st


def set_session_state_keys(*args, **kwargs):
    for key, value in kwargs.items():
        if key not in st.session_state:
            setattr(st.session_state, key, value)
