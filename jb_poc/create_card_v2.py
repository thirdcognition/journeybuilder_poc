import random
import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
from streamlit_extras.stylable_container import stylable_container
from annotated_text import annotated_text, annotation

# Function to generate content for each card + card layout
def gen_content(item):
    with stylable_container(
            key="container_with_border",
            css_styles="""
            {
                border: 0px solid rgba(256, 256, 256, 0.2);
                border-radius: 3rem;
                padding: 2rem;
                background-color: #2e2e2e;
            }
            """,
):
        container = st.container(border=False)
        with container:

            number, text = st.columns([0.1, 0.9])
            with number:
                st.markdown(f"""
                                <div style="font-size: 20px; margin-bottom: 20px; margin-top: 0px; padding: 0px; line-height: 22px;">
                                1.1</div>
                        """, unsafe_allow_html=True)

            with text:
                st.markdown(f"""
                                            <div style="font-size:20px; margin-bottom: 20px; margin-top: 0px; height: 40px; line-height: 22px; padding: 0px;">
                                            Meet the Marketing Team {item['position']} {item['level']}</div>
                                    """, unsafe_allow_html=True)

            lmargin, image, rmargin = st.columns([0.1, 0.8, 0.1])
            with image:
                #Invert image & Fix Contrast
                image = Image.open("sample_image.png")
                st.image(image,use_column_width=True)

            st.markdown(f"""
            <div style="border: 0px solid #fff; padding-left: 20px; border-radius: 0px; text-align: left; height: 90px;">
                <p>{item["type"]} for {item['position']} {item['level']} in {item['location']}.</p>
            </div>
    
            """, unsafe_allow_html=True)

            with stylable_container(
                    key="green_button",
                    css_styles=["""
                    button {
                        background-color: green;
                        border-color: green;
                        color: white;
                        border-radius: 20px;
                    }""",
                    """
                    button:hover {
                        background-color: red;
                        border-color: red;
                        color: white;
                        border-radius: 20px;
                    }
                    """],
            ):
                lmargin, button, rmargin = st.columns([0.1, 0.8, 0.1])
                with button:
                    st.button("Start", key=random.randint(1, 10000), type="primary", use_container_width=True)


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