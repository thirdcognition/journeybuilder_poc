import streamlit as st

def init_sidebar():
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 380px !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True, )

    st.logo("logo.png")
    with st.sidebar:
        st.page_link("main.py", label="Home")
        st.page_link("pages/create_journey.py", label="Create Journey")