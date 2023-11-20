import os
import time
import streamlit as st
import streamlit.components.v1 as components
from functions.on_click import *
from locals.content import *

lc = Content()
def uc_header():
    col201, col202 = st.columns([6, 4])
    with col201:
        st.subheader("📖" + " " + lc.gt("use-case-title"))
    with col202:
        with st.expander(lc.gt("use-case-goal-page")):
            tab1, tab2, tab3 = st.tabs(["Цели страницы ---", "Этапы выполнения---", "Типичные ошибки---"])
            tab1.write("this is tab 1")
            tab1.image("https://static.streamlit.io/examples/dice.jpg")
            tab2.write("this is tab 2")
            tab2.video("https://www.youtube.com/watch?v=ovtxI75g34g")
            tab3.write("this is tab 2")
            tab3.video("https://www.youtube.com/watch?v=ovtxI75g34g")

