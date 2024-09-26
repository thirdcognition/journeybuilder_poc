import streamlit as st
from create_card import gen_content, split_list_into_chunks, create_sample_data
from sidebar import init_sidebar

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded")

# Initialize Sidebar
init_sidebar()

#---- Main Content Area ----
st.header("My Journeys")

# Number of cards on page
num_cards = 5
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