import random
import streamlit as st
from annotated_text import annotated_text, annotation

def get_card():

    type = ["New hire onboarding", "Project onboarding", "Skill development", "Customer onboarding"]
    team = ["Business", "Product", "Sales", "Tech"]
    position = ["Product", "Customer Success", "Account", "Business Development", "Development"]
    level = ["Manager", "Director"]
    location = ["Helsinki", "Stockholm", "New York", "Berlin", "San Fransisco", "Tokyo"]
    modules = random.randint(7, 9)
    length = random.randint(8, 12)
    key = random.randint(1, 1000)
    position_data = {}

    position_data["type"] = random.choice(type)
    position_data["team"] = random.choice(team)
    position_data["position"] = random.choice(position) + " " + random.choice(level)
    position_data["location"] = random.choice(location)
    position_data["modules"] = modules
    position_data["length"] = length

    annotated_text(annotation(position_data["team"] + " Team", "", "#184370"))
    st.subheader(position_data["position"])
    st.markdown(position_data["type"] + " journey for a " + position_data["position"] + ".")
    st.markdown(
        "Modules: " + str(position_data["modules"]) + "  \nEst. Length: " + str(position_data["length"]) + " hours" + "  \nLocation: " +
        position_data["location"])
    st.markdown(" ")
    st.button("View Journey", key=key, type="primary", use_container_width=True)