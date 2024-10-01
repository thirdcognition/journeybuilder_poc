import streamlit as st
from sidebar import init_sidebar
from global_css import init_css
import json, os, openai

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar & Custom CSS & OpenAI
init_sidebar()
init_css()

#---- Main Content Area ----
st.header("User View")
st.markdown(" ")

# AI Role Matcher - Input area
with st.expander("AI Role Matcher - beta", expanded=False, icon="⚡"):
    container = st.container(border=False)
    with container:
        text_input = st.text_area("Role Description", placeholder="Describe role in detail", key=2, height=300)

#Provide OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")#

#Function for LLM response
def get_completion(prompt, model="gpt-4o-2024-08-06"):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0.1,  # this is the degree of randomness of the model's output
  )
  return response.choices[0].message["content"]


# Load JSON data for OpenAI Prompts & Matching
with open('Department_Roles.json', 'r') as f:
    roles = json.load(f)
# Prompt
prompt = f"First, I will give you a list of roles: {roles}, and then I will give you a job description: {text_input}. Then, I want you to give me the role (only from those in {roles}) that matches the job description (in {text_input}) the most. I want the output to only mention the role (one of the roles in {roles}) that closely matches the job description (in {text_input}). I don't want any other explanations in your output:"


#Send prompt when at least 30 characters
if len(text_input) > 30:
    text_input = f"{get_completion(prompt)}"

#--- Select Box ---

#Initialize session state for selected option if it doesn't exist
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

#Load JSON for Template Data
with open('Journey_Templates.json', 'r') as f:
    data = json.load(f)

#Load JSON for Select Box
with open('Journey_Templates.json', 'r') as f:
    data_dict = json.load(f)

# Convert the dictionary keys to a list
roles_list = list(data_dict.keys())

options = roles_list


# Function to update the selected option based on text input
def update_selected_option(text_input):
    matching_options = [option for option in options if text_input.lower() in option.lower()]
    if matching_options:
        st.session_state.selected_option = matching_options[0]
    else:
        st.session_state.selected_option = None

# Update selected option based on text input
update_selected_option(text_input)


# Display the selectbox with the dynamically matched option
selected_option = st.selectbox(
    'Choose an option:',
    options,
    index=options.index(st.session_state.selected_option) if st.session_state.selected_option else 0
)



st.markdown(" ")




# Extract the second level of information
second_level_data = data[selected_option][0]

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
