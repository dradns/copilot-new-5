import os
import time
import streamlit as st
import streamlit.components.v1 as components
from functions.on_click import *

def us_buttons():
    col_us_73, col_us_74,col_us_75 = st.columns([3,3,3])
    with col_us_73:
        st.button("Сохранить", on_click=clear_chat_history, type="primary", key="us101")
    with col_us_74:
        st.button("Улучшить", on_click=clear_chat_history, type="primary", key="us102")
    with col_us_75:
        st.button("Создать UC", on_click=clear_chat_history, type="primary", key="us103")



style = "<style>.row-widget.stButton {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)