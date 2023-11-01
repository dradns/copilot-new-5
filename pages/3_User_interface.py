import streamlit as st
from components.sidebar import sidebar

with st.expander("Задача страницы"):
    st.write("Привет")
    st.image("https://static.streamlit.io/examples/dice.jpg")

with st.expander("Этапы выполнения"):
    st.video("https://www.youtube.com/watch?v=ovtxI75g34g")

with st.expander("Типичные ошибки"):
    st.image("static/2023-10-30_16-10-05.png")


def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

st.button('Forgot context', on_click=clear_chat_history)
st.warning("Lets write couple of use cases")

sidebar()

#st.session_state["API_KEY"] = 'r8_5dXks0XSi27sUU4zxiCeKiYOB1wvfil3UZOxV'
#replicate_api = st.session_state.get("API_KEY")
#os.environ['REPLICATE_API_TOKEN'] = replicate_api
# print('API KEY')
# print(st.session_state.get("API_KEY"))

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "I'm best business analyst ever! Wanna help?"}]

# Display or clear chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
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