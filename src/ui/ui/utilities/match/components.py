import streamlit as st


def add_story_chat():
    user_sentence = st.chat_input(
        "Escribí una oración. Para terminar el juego escribí [FIN]",
        disabled=st.session_state.turn != "user",
        key="user_sentence",
        # on_submit=change_turn,
        args=("bot",),
    )
    st.session_state.story_utterances.append(user_sentence)

    if user_sentence:
        user_message = st.chat_message(name="user", avatar="user")
        user_message.write(user_sentence)

        import time

        # time.sleep(3)
        bot_message = st.chat_message(name="assistant", avatar="assistant")
        bot_message.write(user_sentence)
        # change_turn("user")


def add_story_container():
    st.subheader("Historia", help="Aquí verás la historia creada hasta el momento.")
    with st.container(height=150):
        utterances = st.session_state.story_utterances or []
        story = " ".join(utterances)
        st.text(story)
