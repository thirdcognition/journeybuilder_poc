import streamlit as st
from annotated_text import annotated_text, annotation
from create_card import get_position_data, get_card

# Sidebar
st.logo("logo.png")
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/Create_Journey.py", label="Create Journey")

#PageTitle

st.header("My Journeys")
st.markdown(" ")

#Get Position Data amd Create Cards
number_of_cards = 2



#Static Columns & Rows


col1, col2, col3 = st.columns(3)

with col1:
    container = st.container(border=True)


    with container:
        get_card()


with col2:
    container = st.container(border=True)

    with container:
        get_card()


with col3:
    container = st.container(border=False)


    with container:
        st.markdown(" ")




