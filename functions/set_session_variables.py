import streamlit as st
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()
def set_session_variables():
    #SET LANGUAGE
    if "LANGUAGE" not in st.session_state.keys():
        st.session_state["LANGUAGE"] = 'RUS'
    #SET MODEL
    if "selected_model" not in st.session_state.keys():
        st.session_state["selected_model"] = 'Llama2-13B'
    #SET HISTORY
    if "chat_history" not in st.session_state.keys():
        st.session_state.chat_history = [{"role": "assistant", "content": lc.gt("user-story-ass-first-reply")}]
    # SET US quill content
    if "user_story_quill_content" not in st.session_state.keys():
        st.session_state["user_story_quill_content"] = ""
    # SET US quill content
    if "use_case_quill_content" not in st.session_state.keys():
        st.session_state["use_case_quill_content"] = ""
    # SET AC quill content
    if "acceptance_criteria_quill_content" not in st.session_state.keys():
        st.session_state["acceptance_criteria_quill_content"] = ""

    if "counter" not in st.session_state.keys():
        st.session_state["counter"] = 300
