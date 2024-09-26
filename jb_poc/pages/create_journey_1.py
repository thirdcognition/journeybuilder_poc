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
st.subheader("Journey Details")
container = st.container(border=True)
with container:
    option = st.selectbox(
        "Journey Purpose",
        ("New Hire Onboarding", "Project Onboarding", "Skill Development", "Customer Onboarding", "Other"),
        index=0,
    )

    journey_name = st.text_input("Job Title", placeholder="Account Manager", key=1)

    option = st.selectbox(
        "Location",
        ("Helsinki", "Stockholm", "Berlin", "Tokyo", "Other"),
        index=None,
        placeholder="Choose location",
    )
st.markdown(" ")
st.subheader("Role Details")
container = st.container(border=True)
with container:
    role_description = st.text_area("Role Description", placeholder="Describe role in detail", key=2, height=200)

    col1, col2 = st.columns([0.4,0.6])
    with col1:
        job_description = st.text_input("Link to job description", placeholder="www.linkedin.com", key=3)
    with col2:
        uploaded_files = st.file_uploader("Upload job descritpion (optional)", accept_multiple_files=True)

col1, col2 = st.columns([0.85,0.15])
with col2:
    st.page_link("pages/create_journey_2.py", label="Continue")