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

#---- AI Role Matcher - Start ----
import os
import openai

# Setting the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
def get_completion(prompt, model="gpt-4o-2024-08-06"):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=1,  # this is the degree of randomness of the model's output
  )
  return response.choices[0].message["content"]

with st.expander("AI Role Matcher", expanded=False, icon="⚡"):
    container = st.container(border=False)
    with container:
        # prompt = f"Hello Pirate!"
        # response = f'"{get_completion(prompt)}'""
        #st.markdown(response)
        role_description = st.text_area("Role Description", placeholder="Describe role in detail", key=2, height=300)


#Match Description with position

# Load JSON data
with open('Department_Roles.json', 'r') as f:
    roles = json.load(f)

with open('Journey_Templates.json', 'r') as f:
    data = json.load(f)

prompt = f"First, I will give you a list of roles: {roles}, and then I will give you a job descriptions: {role_description}. Then, I want you to give me the role (only from those in {roles}) that matches the job description (in {role_description}) the most. I want the output to only mention the role (one of the roles in {roles}) that closely matches the job description (in {role_description}). I don't want any other explanations in your output:"

if len(role_description) > 30:
    response = f"Matches with: {get_completion(prompt)}"
else:
    response = "Please provide description"

with container:
    st.markdown(response)


#---- AI Role Matcher - End ----

#--- Select Box ---

# Get all roles for Select Box
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
        subindex = 1
        for sub_title, subsubject in subject.items():
            if subindex != 1:
                st.divider()

            st.subheader(f"{str(index+1)}\.{subindex} {sub_title}")
            subindex += 1

            for item in subsubject:
                col1, col2 = st.columns([0.01, 0.99])
                with col2:
                    st.write(f"- {item}")





# Create expander for every Section
index = 1
for index, key in enumerate(second_level_data.keys()):
    handle_journey_subject(index, key, second_level_data[key][0])
