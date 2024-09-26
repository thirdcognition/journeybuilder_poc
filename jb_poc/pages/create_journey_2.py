import streamlit as st
from sidebar import init_sidebar
from global_css import init_css

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar & Custom CSS
init_sidebar()
init_css()

#---- Main Content Area ----
st.header("Create Journey")
st.markdown(" ")
st.subheader("Include Common Data")
container = st.container(border=True)
with container:
    st.markdown("Mandatory")
    culture = st.checkbox("Introduction to Culture & Values", value=True, disabled=True, key=1)
    conduct = st.checkbox("Introduction to Code of Conduct", value=True, disabled=True, key=2)
    st.divider()
    st.markdown("Optional")
    quality = st.checkbox("Introduction to Quality Policy", value=True, key=3)
    health = st.checkbox("Introduction to Healt & Safety", value=True, key=4)
    human = st.checkbox("Introduction to Human Rights Policy", value=True, key=5)
    environment = st.checkbox("Introduction to Environmental Policy", value=True, key=6)
    whistle = st.checkbox("Introduction to Whistleblowing", value=True, key=7)

col1, col2, col3 = st.columns([0.15, 0.7,0.15])
with col1:
    st.page_link("pages/create_journey_1.py", label="Back")
with col3:
    st.page_link("pages/create_journey_3.py", label="Continue")
