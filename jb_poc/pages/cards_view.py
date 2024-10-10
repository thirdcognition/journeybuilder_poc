import streamlit as st
from create_card_v2 import gen_content, split_list_into_chunks, create_sample_data
from sidebar import init_sidebar
from global_css import init_css
from PIL import Image, ImageOps, ImageEnhance

# Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar & Custom CSS
init_sidebar()
init_css()

# ---- Main Content Area ----

st.markdown("")


st.header("Hello [First Name]")
st.subheader("Here’s what we are learning today!")

##---- Search Bar ----
search_journey = st.text_input(" ", placeholder="Search Onboarding Journey", label_visibility="hidden")
st.markdown("")



# Number of cards on page
num_cards = 3
items = create_sample_data(num_cards)

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

st.markdown("**Time to complete module(s):** 5 Days - You are on track!")

# ##---- Cards ----
# st.subheader("1. Introduction to the Company & Team")
#
# card1, card2, card3 = st.columns(3, gap="small")
#
# with card1:
#     container = st.container(border=True)
#     with container:
#         number, text = st.columns([0.15, 0.85])
#         with number:
#             st.write("**1.1**")
#
#         with text:
#             st.write("**Meet the Marketing Team**")
#
#         lmargin, image, rmargin = st.columns([0.15, 0.7, 0.15])
#         with image:
#
#             # Invert image & Fix Contrast
#             image = Image.open("sample_image.png")
#             inverted_image = ImageOps.invert(image)
#             adjust_contrast = ImageEnhance.Contrast(inverted_image)
#             adjusted_image = adjust_contrast.enhance(0.71)
#             st.image(adjusted_image, width=128)
#
#         lmargin, intro, rmargin = st.columns([0.1, 0.8, 0.1])
#         with intro:
#             st.caption("Introduction to the marketing team members and their roles.")
#             st.markdown("")
#
#         lmargin, button, rmargin = st.columns([0.325, 0.40, 0.275])
#         with button:
#             st.button("Start")
