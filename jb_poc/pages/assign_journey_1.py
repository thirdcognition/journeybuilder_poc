import streamlit as st
from sidebar import init_sidebar

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar
init_sidebar()

#---- Main Content Area ----
st.header("Assign Journey")
st.markdown(" ")

st.subheader("Choose Journey")
container = st.container(border=True)
with container:
    choose = st.multiselect(
        "Select Journey",
        ["GDPR Policy Introduction", "Customer Success Manager - Onboarding", "Business Development - Onboarding", "Introduction to Coding Standards", "Introduction to Brand Values"])

st.markdown(" ")
st.subheader("Assign Journey")
container = st.container(border=True)
with container:
    assign_to = st.multiselect(
        "Assign Journey to",
        ["Individual(s)", "Team(s)", "Department(s)", "Location(s)", "Subsidiary"],
        ["Individual(s)", "Team(s)"],)
    st.divider()

    st.subheader("Assign to Individual(s)")
    emp_id = st.text_input("Employee Details (Name or ID)", placeholder="eg. XH12345", key=1)
    st.button("+ Add Employee", type="primary")
    st.divider()

    st.subheader("Assign to Team(s)")
    team_id = st.multiselect(
        "Team Description / Function",
        ["Sales", "Product", "Marketing", "Research", "Technology", "C-Level"],)
    st.markdown(" ")


col1, col2, col3 = st.columns([0.15, 0.7,0.15])
with col3:
    st.page_link("main.py", label="Continue")