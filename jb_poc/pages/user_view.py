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

# Create expander for every Section
order = 1
for key in second_level_data.keys():
    with st.expander(f"{order} - {key}"):
        st.write(second_level_data[key])
        order += 1