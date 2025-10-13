import streamlit as st

from ui.ui_components.sidebar import set_sidebar
from ui.utilities.session_state import set_session_state_keys


set_session_state_keys(stage=0)

st.title("Cadáver Exquisito")
set_sidebar()

with st.container(height=300):
    st.markdown("hola" * 5000)
