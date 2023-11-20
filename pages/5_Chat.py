import os
import streamlit as st
from functions.LLM_model import *
from locals.prompt import *
from locals.content import *
from functions.collect_instructions import *
from functions.collect_message_history import *
from functions.set_session_variables import *

lc = Content()
pt = Prompt()

#SET SESSION VARIABLES
set_session_variables()

#TITLES
page_name = "use-case"
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    del st.session_state["messages_uc"]
    if 'messages_uc' not in st.session_state:
        st.session_state['messages_uc'] = [{"role": "assistant", "content": lc.gt("use-case-ass-first-reply")}]

#USAGE BUTTON RESET HISTORY
st.button(lc.gt("use-case-button-forget"), on_click=clear_chat_history, type="primary", key=2020)

# Store LLM generated responses
if "messages_uc" not in st.session_state.keys():
    st.session_state.messages_uc = [{"role": "assistant", "content": lc.gt("use-case-ass-first-reply")}]

# Display or clear chat history
for message in st.session_state.messages_uc:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#append user message to global
if user_prompt := st.chat_input():
    st.session_state.messages_uc.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages_uc[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner(lc.gt("thinking")):
            response = model_response(user_prompt, page_name)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages_uc.append(message)