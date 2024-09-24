import streamlit as st

st.logo("logo.png")

# Using "with" notation
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/Create_Journey.py", label="Create Journey")


st.header("Create Journey")