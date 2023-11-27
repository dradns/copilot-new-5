import os
import streamlit as st
from functions.LLM_model import *
from locals.prompt import *
from locals.content import *
from functions.collect_instructions import *
from functions.collect_message_history import *
from functions.set_session_variables import *
import openai

openai.api_key = "sk-or-vv-d61e59a8dfa7d3902916bf78955555c9e1da1acaaae901c14f7d0bfeed0ca059" # ваш ключ в VseGPT после регистрации
openai.base_url = "https://api.vsegpt.ru:6070/v1/"

def resp(history):
    response = openai.chat.completions.create(
        model = "meta-llama/llama-2-70b-chat",
        messages=history,
        temperature=0.7,
        n=1,
        max_tokens=int(500),
        #stream=True
    )
    return response


def model_stream(user_prompt):
    string_dialogue_before = ""
    for dict_message in st.session_state["new_chat"]:
        if dict_message["role"] == "user":
            string_dialogue_before += "User: " + dict_message["content"] + "\n"
        else:
            string_dialogue_before += "Assistant: " + dict_message["content"] + "\n"
    history = f"{string_dialogue_before}"
    print(history)
    return openai.chat.completions.create(
        model="meta-llama/llama-2-70b-chat",
        messages=st.session_state["new_chat"],
        temperature=0.7,
        n=1,
        max_tokens=512,
        stream=True
    )

lc = Content()
pt = Prompt()

#SET SESSION VARIABLES
set_session_variables()

#TITLES
page_name = "chat"
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")

#DECLARE BUTTON RESET HISTORY
def clear_chat_history():
    del st.session_state["new_chat"]
    if 'new_chat' not in st.session_state:
        st.session_state['new_chat'] = [{"role": "assistant", "content": lc.gt("use-case-ass-first-reply")}]

#USAGE BUTTON RESET HISTORY
st.button(lc.gt("use-case-button-forget"), on_click=clear_chat_history, type="primary", key=2020)

# Store LLM generated responses
if "new_chat" not in st.session_state.keys():
    st.session_state.new_chat = [{"role": "assistant", "content": lc.gt("say-hi")}]

# Display or clear chat history
for message in st.session_state.new_chat:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#append user message to global
if user_prompt := st.chat_input():
    st.session_state.new_chat.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

# Generate a new response if last message is not from assistant
if st.session_state.new_chat[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner(lc.gt("thinking")):
            response = model_stream(user_prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item.choices[0].delta.content
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.new_chat.append(message)

# st.write('session_state.keys')
# st.write(st.session_state)


