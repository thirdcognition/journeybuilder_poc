import streamlit as st
from annotated_text import annotated_text, annotation

st.logo("logo.png")

# Using "with" notation
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/Create_Journey.py", label="Create Journey")

#PageTitle

st.header("My Journeys")
st.markdown(" ")

#List Journeys

col1, col2, col3 = st.columns(3)


with col1:
    container = st.container(border=True)

    with container:
        annotated_text(annotation("Business Team","" , "#184370"))
        st.subheader("Senior Account Manager")
        st.markdown("Onboarding journey for a Senior Account Manager.")
        st.markdown("Modules: 5  \nEst. Length: 12h  \nLocation: New York")
        st.markdown(" ")

        st.button("View Journey", key=1, type="primary", use_container_width=True,)



with col2:
    container = st.container(border=True)

    with container:
        annotated_text(annotation("Product Team", "", "#184370"))
        st.subheader("Senior Product Manager")
        st.markdown("Onboarding journey for a Senior Product Manager.")
        st.markdown("Modules: 7  \nEst. Length: 13h  \nLocation: Helsinki")
        st.markdown(" ")

        st.button("View Journey", key=2, type="primary", use_container_width=True, )

with col3:
    container = st.container(border=True)

    with container:
        annotated_text(annotation("HR Team", "", "#184370"))
        st.subheader("Chief Talent Officer")
        st.markdown("Onboarding journey for Chief Talent Officer.")
        st.markdown("Modules: 9  \nEst. Length: 15h  \nLocation: Helsinki")
        st.markdown(" ")

        st.button("View Journey", key=3, type="primary", use_container_width=True)



