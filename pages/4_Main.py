import streamlit as st
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide") #, initial_sidebar_state="collapsed"

from functions.set_session_variables import *
from components.sidebar import *
from components.us.us_buttons import *
from components.us.us_header import *
from components.uc.uc_buttons import *
from components.uc.uc_header import *
from components.uc.uc_quill import *
from components.ac.ac_buttons import *
from components.ac.ac_header import *
from components.ac.ac_quill import *

#DECLARE SESSION VARIABLES
set_session_variables()

#DECLARE CONFIG
page_name = "requirements"

#RENDER USER STORY HEADER
us_header()
#USER STORY TEXT AREA COLUMNS
us_tx_c1, us_tx_c2, us_tx_c3, us_tx_c4 = st.columns([8, 0.00001, 0.00001, 0.00001])
with us_tx_c1:
    us_text_area = st.empty()
    us_text_area.text_area(label="", height=st.session_state["user_story_height"],
                           placeholder=st.session_state["user_story_placeholder"], key="tx-user-story-key", on_change=clear_chat_history())

# USER STORY BUTTONS
us_bt_c1, us_bt_c2, us_bt_c3, us_bt_c4, us_bt_c5 = st.columns([33, 33, 0.01, 33, 0.01])
with us_bt_c1:
    if st.button("Cгенерировать US", type="secondary", key="us_bt_generate"):
        with st.spinner(lc.gt("thinking")):
            res = model_button_response(st.session_state.get("tx-user-story-key"),"user-story")
            st.session_state["current_us"] = res
            us_text_area.text_area("", value=st.session_state["current_us"], height=st.session_state["user_story_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

with us_bt_c2:
    if st.button("Улучшить US", type="secondary", key="us_bt_improve"):
        with st.spinner(lc.gt("thinking")):
            res = model_improve_us()
            st.session_state["improved_us"] = res
            us_text_area.text_area("", value=st.session_state["improved_us"], height=st.session_state["user_story_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

# with us_bt_c3:
#     if st.button("Покритиковать US", type="secondary", key="us_bt_critique"):
#         st.session_state["counter"] += 1
#         us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
#         style = "<style>.row-widget.stButton {text-align: center;}</style>"
#         st.markdown(style, unsafe_allow_html=True)

with us_bt_c4:
    if st.button("Создать UC", type="secondary", key="us_bt_create_UC"):
        with st.spinner(lc.gt("thinking")):
            res = model_generate_uc()
            st.session_state["generated_uс"] = res
            #us_text_area.text_area("", value=st.session_state["improved_us"], height=st.session_state["user_story_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

# with us_bt_c5:
#     if st.button("Cохранить", type="secondary", key="us_bt_save"):
#         st.session_state["counter"] += 1
#         us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
#         style = "<style>.row-widget.stButton {text-align: center;}</style>"
#         st.markdown(style, unsafe_allow_html=True)

#END OF USER STORY
#RENDER USER STORY BUTTONS
st.divider()

#RENDER USE CASE HEADER
uc_header()

#USE CASE TEXT AREA COLUMNS
uc_tx_c1, uc_tx_c2, uc_tx_c3, uc_tx_c4 = st.columns([8, 0.00001, 0.00001, 0.00001])
with uc_tx_c1:
    uc_text_area = st.empty()
    uc_text_area.text_area(label="", height=st.session_state["use_case_height"],
                           value=st.session_state["generated_uс"], key="tx-use-case-key", on_change=clear_chat_history())

# USE CASE BUTTONS
uc_bt_c1, uc_bt_c2, uc_bt_c3, uc_bt_c4, uc_bt_c5 = st.columns([25, 25, 25, 25, 25])
with uc_bt_c1:
    if st.button("Cгенерировать AC", type="secondary", key="uc_bt_generate"):
        #st.session_state["counter"] += 1
        # print("------------------")
        # print(st.session_state.get("tx_first"))
        # print("------------------")
        with st.spinner(lc.gt("thinking")):
            res = model_button_response(st.session_state.get("tx-use-case-key"),"use-case")
            st.session_state["current_us"] = res
            #print(st.session_state["tx_first"])
            us_text_area.text_area("", value=st.session_state["current_us"], height=st.session_state["use_case_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

with uc_bt_c2:
    if st.button("Улучшить UC", type="secondary", key="uc_bt_improve"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c3:
    if st.button("Покритиковать UC", type="secondary", key="uc_bt_critique"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c4:
    if st.button("Создать AC", type="secondary", key="uc_bt_create_UC"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c5:
    if st.button("Cохранить", type="secondary", key="uc_bt_save"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

#END OF USE CASE
st.divider()

#RENDER USE CASE HEADER
ac_header()

#ACCEPTANCE CRITERIA TEXT AREA COLUMNS
ac_tx_c1, ac_tx_c2, ac_tx_c3, ac_tx_c4 = st.columns([8, 0.00001, 0.00001, 0.00001])
with ac_tx_c1:
    ac_text_area = st.empty()
    ac_text_area.text_area(label="", height=st.session_state["acceptance_criteria_height"],
                           placeholder=st.session_state["acceptance_criteria_placeholder"], key="tx-acceptance-criteria-key", on_change=clear_chat_history())

# ACCEPTANCE CRITERIA BUTTONS
ac_bt_c1, ac_bt_c2, ac_bt_c3, ac_bt_c4, ac_bt_c5 = st.columns([25, 25, 25, 25, 25])
with ac_bt_c1:
    if st.button("Cгенерировать AC", type="secondary", key="ac_bt_generate"):
        with st.spinner(lc.gt("thinking")):
            res = model_button_response(st.session_state.get("tx-acceptance-criteria-key"),"acceptance-criteria")
            st.session_state["current_us"] = res
            ac_text_area.text_area("", value=st.session_state["current_ac"], height=st.session_state["acceptance_criteria_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

with ac_bt_c2:
    if st.button("Улучшить AC", type="secondary", key="ac_bt_improve"):
        with st.spinner(lc.gt("thinking")):
            res = model_button_response(st.session_state.get("tx-acceptance-criteria-key"),"acceptance-criteria")
            st.session_state["current_us"] = res
            ac_text_area.text_area("", value=st.session_state["current_ac"], height=st.session_state["acceptance_criteria_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

with ac_bt_c3:
    if st.button("Покритиковать AC", type="secondary", key="ac_bt_critique"):
        st.session_state["counter"] += 1
        ac_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["acceptance_criteria_height"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with ac_bt_c4:
    if st.button("Создать UC", type="secondary", key="ac_bt_create_UC"):
        st.session_state["counter"] += 1
        ac_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["acceptance_criteria_height"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with ac_bt_c5:
    if st.button("Cохранить", type="secondary", key="ac_bt_save"):
        st.session_state["counter"] += 1
        ac_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["acceptance_criteria_height"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

#END OF USER STORY
#RENDER USER STORY BUTTONS
st.divider()

#DEBUG
st.write('session_state.keys')
st.write(st.session_state)