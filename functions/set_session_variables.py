import streamlit as st
from locals.prompt import *
from locals.content import *

lc = Content()
pt = Prompt()

user_story_placeholder = """Пользовательская история это короткое простое описание фунционала, описанное от лица ПЕРСОНЫ, которая желает получить новые возможности системы, Например: 'Как пользователь <тип ПОЛЬЗОВАТЕЛЯ>, Я хочу <такую-то ЦЕЛЬ> для того чтобы <определенная ПРИЧИНА/ПОТРЕБНОСТЬ >"""
use_case_placeholder = """Пример пользовательского сценария для ситуации, когда домработница стирает белье:
                        Участники — Жители, домработница и т.д.
                        Основной участник — Домработница
                        Цели — Постирать белье, сложить все предметы, при необходимости погладить одежду
                        Предусловия — Сегодня пятница, и в прачечной есть белье
                
                        Основной флоу для этого пользовательского сценария:
                        Домработница приходит в прачечную в пятницу.Она приводит прачечную в порядок. 
                        После этого она стирает и сушит белье в каждой загрузки стиральной машины.
                        Она складывает вещи, которые нужно сложить, затем гладит и вешает мятые предметы.
                
                        Альтернативные флоу:
                        Домработница гладит любые помятые вещи перед тем, как повесить их на вешалку.
                        Домработница перестирывает все вещи, которые посчитает грязными.\n",
"""

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
    if "user_story_placeholder" not in st.session_state.keys():
        st.session_state["user_story_placeholder"] = user_story_placeholder
    if "use_case_placeholder" not in st.session_state.keys():
        st.session_state["use_case_placeholder"] = use_case_placeholder
    # SET US quill content
    if "use_case_quill_content" not in st.session_state.keys():
        st.session_state["use_case_quill_content"] = ""
    # SET AC quill content
    if "acceptance_criteria_quill_content" not in st.session_state.keys():
        st.session_state["acceptance_criteria_quill_content"] = ""
    if "counter" not in st.session_state.keys():
        st.session_state["counter"] = 300
    if "user_story_height" not in st.session_state.keys():
        st.session_state["user_story_height"] = 200
    if "use_case_height" not in st.session_state.keys():
        st.session_state["use_case_height"] = 350
    if "acceptance_criteria_height" not in st.session_state.keys():
        st.session_state["acceptance_criteria_height"] = 300
