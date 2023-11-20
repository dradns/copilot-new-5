import os
import time
import streamlit as st
import streamlit.components.v1 as components
from functions.on_click import *

def ac_buttons():
    col_ac_373, col_ac_374,col_ac_375 = st.columns([3,3,3])
    with col_ac_373:
        st.button("Сохранить", on_click=clear_chat_history, type="primary", key="uc301")
    with col_ac_374:
        st.button("Улучшить", on_click=clear_chat_history, type="primary", key="uc302")
    with col_ac_375:
        st.button("Самолет", on_click=clear_chat_history(), type="primary", key="uc303")


style = "<style>.row-widget.stButton {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)