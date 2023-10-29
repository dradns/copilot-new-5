import os
import streamlit as st
from components.sidebar import sidebar
import streamlit_mermaid as stmd

from st_pages import Page, show_pages, Section, add_page_title
#add_page_title()

# Enable caching for expensive functions
#bootstrap_caching()

sidebar()

code = """
sequenceDiagram
    participant Client
    participant Server
    participant Database

    Client->>Server: Request (Post Status Update)
    Server->>Database: Insert Status Update
    Database-->>Server: Acknowledge Insert
    Server-->>Client: Response (Status Update Successful)
"""

code = """
    graph LR
    A[Start] --> B(Mermaid World) --> C(Underwater City) --> D(Mermaid's Home)
"""

mermaid = stmd.st_mermaid(code)
st.write(mermaid)
