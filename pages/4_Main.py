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
us_bt_c1, us_bt_c2, us_bt_c3, us_bt_c4, us_bt_c5 = st.columns([25, 25, 25, 25, 25])
with us_bt_c1:
    if st.button("Cгенерировать US", type="primary", key="us_bt_generate"):
        #st.session_state["counter"] += 1
        # print("------------------")
        # print(st.session_state.get("tx_first"))
        # print("------------------")
        with st.spinner(lc.gt("thinking")):
            res = model_button_response(st.session_state.get("tx-user-story-key"),"user-story")
            st.session_state["current_us"] = res
            #print(st.session_state["tx_first"])
            us_text_area.text_area("", value=st.session_state["current_us"], height=st.session_state["user_story_height"])
            style = "<style>.row-widget.stButton {text-align: center;}</style>"
            st.markdown(style, unsafe_allow_html=True)

with us_bt_c2:
    if st.button("Улучшить US", type="primary", key="us_bt_improve"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with us_bt_c3:
    if st.button("Покритиковать US", type="primary", key="us_bt_critique"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with us_bt_c4:
    if st.button("Создать UC", type="primary", key="us_bt_create_UC"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with us_bt_c5:
    if st.button("Cохранить", type="primary", key="us_bt_save"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

#END OF USER STORY
#RENDER USER STORY BUTTONS
st.divider()
st.divider()
st.divider()
st.divider()
st.divider()

#RENDER USE CASE HEADER
uc_header()

#USE CASE TEXT AREA COLUMNS
uc_tx_c1, uc_tx_c2, uc_tx_c3, uc_tx_c4 = st.columns([8, 0.00001, 0.00001, 0.00001])
with uc_tx_c1:
    uc_text_area = st.empty()
    uc_text_area.text_area(label="", height=st.session_state["use_case_height"],
                           placeholder=st.session_state["use_case_placeholder"], key="tx-use-case-key", on_change=clear_chat_history())

# USE CASE BUTTONS
uc_bt_c1, uc_bt_c2, uc_bt_c3, uc_bt_c4, uc_bt_c5 = st.columns([25, 25, 25, 25, 25])
with uc_bt_c1:
    if st.button("Cгенерировать AC", type="primary", key="uc_bt_generate"):
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
    if st.button("Улучшить UC", type="primary", key="uc_bt_improve"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c3:
    if st.button("Покритиковать UC", type="primary", key="uc_bt_critique"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c4:
    if st.button("Создать AC", type="primary", key="uc_bt_create_UC"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

with uc_bt_c5:
    if st.button("Cохранить", type="primary", key="uc_bt_save"):
        st.session_state["counter"] += 1
        us_text_area.text_area("", value=st.session_state["counter"], height=st.session_state["counter"])
        style = "<style>.row-widget.stButton {text-align: center;}</style>"
        st.markdown(style, unsafe_allow_html=True)

#RENDER USE CASE HEADER
ac_header()
#RENDER QUILL FOR USE CASE
# x = st.empty()
# x.info("initial text")
# if st.checkbox("Check to redraw"):
#     x.info("redraw")

# y = st.empty()
# y.markdown()
# if st.checkbox("Check to redraw"):
#     y.info("redraw")
#
# if st.button("Самолет", type="primary", key="uc307"):
#     tmp = st.session_state['acceptance_criteria_quill_content']
#     ac_quill()


#RENDER USE CASE BUTTONS
ac_buttons()





#DEBUG
st.write('session_state.keys')
st.write(st.session_state)