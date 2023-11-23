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

acceptance_criteria_placeholder = """На странице товара доступна кнопка “заказать” (во всех браузерах, включая мобильную версию)
При нажатии на кнопку “заказать” в всплывающем окне показывается форма заказа (во всех браузерах, включая мобильную версию)
Форма заказа содержит следующие поля (перечислить поля…)
Форма оснащена валидацией данных (например, в поле “телефон” нельзя ввести текст…)
При заполнении всех обязательных полей заказа и нажатии кнопки “отправить заказ” клиенту приходит сообщение “об отправке заказа”
При заполнении всех обязательных полей заказа и нажатии кнопки “отправить заказ” администратор сайта получает уведомление и всю информацию о заказе, заполненную клиентом, по email.
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

    # SET US content
    if "user_story_placeholder" not in st.session_state.keys():
        st.session_state["user_story_placeholder"] = user_story_placeholder
    if "improved_us" not in st.session_state.keys():
        st.session_state["improved_us"] = ""
    if "tx-user-story-key-improved" not in st.session_state.keys():
        st.session_state["tx-user-story-key-improved"] = ""

    # SET UС content
    if "generated_uс" not in st.session_state.keys():
        st.session_state["generated_uс"] = ""
    if "use_case_placeholder" not in st.session_state.keys():
        st.session_state["use_case_placeholder"] = use_case_placeholder
    if "improved_uс" not in st.session_state.keys():
        st.session_state["improved_uс"] = ""

    # SET AС content
    if "acceptance_criteria_placeholder" not in st.session_state.keys():
        st.session_state["acceptance_criteria_placeholder"] = acceptance_criteria_placeholder
    if "generated_aс" not in st.session_state.keys():
        st.session_state["generated_aс"] = ""
    if "improved_aс" not in st.session_state.keys():
        st.session_state["improved_aс"] = ""

    if "counter" not in st.session_state.keys():
        st.session_state["counter"] = 300
    if "user_story_height" not in st.session_state.keys():
        st.session_state["user_story_height"] = 200
    if "use_case_height" not in st.session_state.keys():
        st.session_state["use_case_height"] = 350
    if "acceptance_criteria_height" not in st.session_state.keys():
        st.session_state["acceptance_criteria_height"] = 300
