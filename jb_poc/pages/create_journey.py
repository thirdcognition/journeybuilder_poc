import streamlit as st
from sidebar import init_sidebar

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar
init_sidebar()

#---- Main Content Area ----
st.header("Create Journey")