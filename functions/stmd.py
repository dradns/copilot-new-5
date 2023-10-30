import os

import streamlit as st
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_streamlit_mermaid = components.declare_component("streamlit_mermaid", path=build_dir)


def st_mermaid(code: str, width="auto", height="250px", key=None):
    return _streamlit_mermaid(code=code, width=width, height=height, key=key)
