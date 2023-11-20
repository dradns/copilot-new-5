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

#DECLARE SESSION VARIABLES
set_session_variables()

#DECLARE CONFIG
page_name = "requirements"

#RENDER USER STORY HEADER
us_header()
#RENDER QUILL FOR USER STORY
us_quill()
#RENDER USER STORY BUTTONS
us_buttons()
st.divider()
st.warning(" ")
#RENDER USER STORY HEADER
uc_header()
#RENDER QUILL FOR USER STORY
uc_quill()
#RENDER USER STORY BUTTONS
uc_buttons()





#DEBUG
st.write('session_state.keys')
st.write(st.session_state)