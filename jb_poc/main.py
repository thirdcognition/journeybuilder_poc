import streamlit as st
import random
from annotated_text import annotated_text, annotation

# Sidebar
st.logo("logo.png")
with st.sidebar:
    st.page_link("main.py", label="Home")
    st.page_link("pages/Create_Journey.py", label="Create Journey")

# PageTitle
st.header("My Journeys")
st.markdown(" ")

# Function to generate content for each card
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


# Create Sample data for the cards

type = ["New hire onboarding", "Project onboarding", "Skill development", "Customer onboarding"]
team = ["Business", "Product", "Sales", "Tech"]
position = ["Product", "Customer Success", "Account", "Business Development", "Development"]
level = ["Manager", "Director"]
location = ["Helsinki", "Stockholm", "New York", "Berlin", "San Fransisco", "Tokyo"]

# Number of cards on page
num_cards = 5
items = []

for x in range(num_cards):
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


# items = [
#     {'title': 'Card 1', 'description': 'Description for card 1'},
#     {'title': 'Card 2', 'description': 'Description for card 2'},
#     {'title': 'Card 3', 'description': 'Description for card 3'},
#     {'title': 'Card 4', 'description': 'Description for card 4'},
#     {'title': 'Card 5', 'description': 'Description for card 5'},
#     {'title': 'Card 6', 'description': 'Description for card 6'},
# ]


# Function to split the list into chunks
def split_list_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


# Define the number of columns per row
row_len = 3

# Split the items into chunks
item_chunks = split_list_into_chunks(items, row_len)

# Create two rows
for item_row in item_chunks[:2]:  # We only want two rows
    row = st.container()
    cols = row.columns(row_len)
    for i in range(min(row_len, len(item_row))):
        with cols[i]:
            gen_content(item_row[i])


