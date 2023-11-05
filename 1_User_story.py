import os
import streamlit as st
from components.sidebar import sidebar
from functions.llama2 import model_response
from huggingface_hub import InferenceClient
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

#TITLES
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")
st.title("📖"+ lc.gt("user-story-title"))
st.write("")
#st.header('Test 1')
#st.subheader('Test 1')


#st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

with st.expander(lc.gt("user-story-goal-page")):
    st.write("Привет")
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.write("")

with st.expander(lc.gt("user-story-steps")):
    st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

st.write("")

with st.expander(lc.gt("user-story-typical-mistakes")):
    st.image("static/2023-10-30_16-10-05.png")

st.divider()

st.warning(lc.gt("user-story-lets-write"))

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]
#USAGE BUTTON RESET HISTORY
st.button(lc.gt("user-story-button-forget"), on_click=clear_chat_history)

# Enable caching for expensive functions
#bootstrap_caching()
# Render sidebar
sidebar()

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Display or clear chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#append user message to global
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)


