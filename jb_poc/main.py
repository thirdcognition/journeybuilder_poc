import streamlit as st
from annotated_text import annotated_text, annotation
from create_card import get_position_data

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


- check rows based on cards




#Static Columns & Rows


col1, col2, col3 = st.columns(3)

with col1:
    container = st.container(border=True)


    with container:
        data = get_position_data()
        annotated_text(annotation(data["team"] + " Team","" , "#184370"))
        st.subheader(data["position"])
        st.markdown(data["type"] + " journey for a " + data["position"]+".")
        st.markdown("Modules: " + str(data["modules"]) + "  \nEst. Length: " + str(data["length"]) + " hours" + "  \nLocation: " + data["location"])
        st.markdown(" ")
        st.button("View Journey", key=1, type="primary", use_container_width=True,)


with col2:
    container = st.container(border=True)

    with container:
        data2 = get_position_data()
        annotated_text(annotation(data2["team"] + " Team","" , "#184370"))
        st.subheader(data2["position"])
        st.markdown(data2["type"] + " journey for a " + data2["position"]+".")
        st.markdown("Modules: " + str(data2["modules"]) + "  \nEst. Length: " + str(data2["length"]) + " hours" + "  \nLocation: " + data2["location"])
        st.markdown(" ")
        st.button("View Journey", key=2, type="primary", use_container_width=True,)


with col3:
    container = st.container(border=False)


    with container:
        st.markdown(" ")




