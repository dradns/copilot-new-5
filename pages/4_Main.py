import streamlit as st
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide", initial_sidebar_state="collapsed")

from functions.set_session_variables import *
from components.sidebar import *
from components.us.us_buttons import *
from components.us.us_header import *
from components.us.us_quill import *
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


x = st.empty()
x.text_area("Text to translate", value=st.session_state["counter"], height = st.session_state["counter"])

if st.button("Самолет", type="primary", key="uc307"):
    st.session_state["counter"] += 1
    x.text_area("Text to translate", value=st.session_state["counter"], height = st.session_state["counter"])

#RENDER USER STORY HEADER
us_header()
#RENDER QUILL FOR USER STORY
us_quill()
#RENDER USER STORY BUTTONS
us_buttons()
st.divider()
st.warning(" ")


#RENDER USE CASE HEADER
uc_header()
#RENDER QUILL FOR USE CASE
uc_quill()
#RENDER USE CASE BUTTONS
uc_buttons()
st.divider()
st.warning(" ")

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