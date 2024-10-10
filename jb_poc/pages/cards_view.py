import streamlit as st
from sidebar import init_sidebar
from global_css import init_css

# Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded", layout="wide")

# Initialize Sidebar & Custom CSS
init_sidebar()
init_css()

# ---- Main Content Area ----

st.markdown("")

col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col2:
    container = st.container(border=True)
    with container:

        st.header("Hello [First Name]")
        st.subheader("Here’s what we are learning today!")

    ##---- Search Bar ----
        search_journey = st.text_input(" ", placeholder="Search Onboarding Journey", label_visibility="hidden")

