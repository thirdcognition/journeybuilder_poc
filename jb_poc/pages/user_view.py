import streamlit as st
from sidebar import init_sidebar
from global_css import init_css
import json

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar & Custom CSS
init_sidebar()
init_css()

#---- Main Content Area ----
st.header("User View")
st.markdown(" ")

# Load JSON data
with open('Journey_Templates.json', 'r') as f:
    data = json.load(f)

# Get all roles
all_roles = data.keys()

#Select Role
selected_role = st.selectbox(
    "Select Role",
    (all_roles),
    index=0,
)

st.markdown(" ")

# Extract the second level of information
second_level_data = data[selected_role][0]

def handle_journey_subject(index:int, title:str, subject:dict):
    with st.expander(f"{str(index+1)}\. {title}"):
        #st.write(subject)
        for sub_title, subsubject in subject.items():
            st.subheader(sub_title)
            for item in subsubject:
                st.write(item)
        #order += 1

# Create expander for every Section
order = 1
for index, key in enumerate(second_level_data.keys()):
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        handle_journey_subject(index, key, second_level_data[key][0])
    with col2:
        st.page_link("main.py", label="Edit")