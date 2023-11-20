import streamlit as st
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide", initial_sidebar_state="expanded")

from functions.set_session_variables import *
from components.sidebar import *
from components.us.us_buttons import *
from components.us.us_header import *
from components.us.us_quill import *

#DECLARE SESSION VARIABLES
set_session_variables()

#DECLARE CONFIG
page_name = "requirements"

#RENDER US HEADER
us_header()

#RENDER US QUILL
us_quill()

#RENDER US BUTTONS
us_buttons()

#DEBUG
st.write('session_state.keys')
st.write(st.session_state)