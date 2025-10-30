import streamlit as st

from ui.utilities.match.components import add_story_chat, add_story_container
from ui.utilities.session_state import set_session_state_keys


set_session_state_keys(turn="user", story_utterances=[])

st.set_page_config(
    page_title="Match",
    page_icon=":video_game:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={},
)

st.title("Match")
add_story_container()
add_story_chat()
