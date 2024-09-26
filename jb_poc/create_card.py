import random
import streamlit as st
from annotated_text import annotated_text, annotation

# Function to generate content for each card + card layout
def gen_content(item):
    container = st.container(border=True, height=350)
    with container:
        annotated_text(annotation(item["team"] + " Team", "", "#184370"))

        st.markdown(f"""
                <div style="font-size: 20px; margin-bottom: 0px; margin-top: 0px; height: 40px; line-height: 22px;">
                {item['position']} {item['level']}</div>
        """, unsafe_allow_html=True)
        st.columns(1, vertical_alignment="bottom")

        st.markdown(f"""
        <div style="border: 0px solid #ddd; padding: 3px; border-radius: 0px; text-align: left; height: 90px;">
            <p>{item["type"]} for {item['position']} {item['level']} in {item['location']}.</p>
        </div>
         <div style="border: 0px solid #ddd; font-size: 14px; padding: 3px; margin-top: 5px; border-radius: 0px; text-align: left; height: 80px; margin-bottom: 5px;">
            Modules: {item["modules"]}<br>Length:  {item['length']}<br>Location: {item['location']}
        </div>

        """, unsafe_allow_html=True)

        st.button("View Journey", key=random.randint(1, 10000), type="primary", use_container_width=True)

# Function to split the list into chunks
def split_list_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


# Function for creating sample data for cards
def create_sample_data(num):

    type = ["New hire onboarding", "Project onboarding", "Skill development", "Customer onboarding"]
    team = ["Business", "Product", "Sales", "Tech"]
    position = ["Product", "Customer Success", "Account", "Business Development", "Development"]
    level = ["Manager", "Director"]
    location = ["Helsinki", "Stockholm", "New York", "Berlin", "San Fransisco", "Tokyo"]
    items = []

    for x in range(num):
        random_type = random.choice(type)
        random_team = random.choice(team)
        random_position = random.choice(position)
        random_level = random.choice(level)
        random_location = random.choice(location)
        modules = random.randint(7, 9)
        length = random.randint(8, 12)
        new_item = {"team": random_team, "position": random_position, "level": random_level, "type": random_type,
                    "location": random_location, "modules": modules, "length": length}
        items.append(new_item)

    return items