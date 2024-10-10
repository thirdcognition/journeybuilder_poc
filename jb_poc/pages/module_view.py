import streamlit as st
from sidebar import init_sidebar
from global_css import init_css
from PIL import Image, ImageOps, ImageEnhance

#Page Config
st.set_page_config(page_title="Journey Builder", initial_sidebar_state="expanded", layout="wide")

# Initialize Sidebar & Custom CSS
init_sidebar()
init_css()

#---- Main Content Area ----
st.markdown("")
col1, col2, col3 = st.columns([0.1,0.8, 0.1])

with col2:
    container = st.container(border=True)
    with container:
        cont_col1, cont_col2, cont_col3 = st.columns([0.15, 0.8, 0.05], gap="small")

        with cont_col1:

            #Invert image & Fix Contrast
            image = Image.open("sample_image.png")
            inverted_image = ImageOps.invert(image)
            adjust_contrast = ImageEnhance.Contrast(inverted_image)
            adjusted_image = adjust_contrast.enhance(0.71)
            st.image(adjusted_image, width=128)

        with cont_col2:
            st.header("1. Introduction to the Company & Team")
            st.subheader("1.1. Meet the Marketing Team")
            st.markdown("")
            st.write("**Schedule Meetings:**")
            st.write("- Coordinate with the marketing department to schedule one-on-one meetings with each team member. Use a shared calendar or contact each member directly to find suitable times. Ensure that these meetings are spread out over the week to allow sufficient time for meaningful conversations.")
            st.write("**Prepare Introduction:**")
            st.write("- Prepare a brief introduction about yourself, including your role, background, and any relevant experience. Be ready to share your expectations and goals for collaborating with the marketing team.")
            st.write("**One-on-One Meetings:**")
            st.write("- Meet with each team member individually. Use this time to learn about their specific roles, responsibilities, and current projects. Ask questions to understand their daily tasks, challenges, and how they contribute to the overall marketing strategy. Take notes on key points discussed during each meeting.")
            st.write("**Team Meeting:**")
            st.write("- Attend a team meeting to observe the dynamics and communication within the marketing department. Introduce yourself to the entire team and express your enthusiasm for working together.")
            st.markdown("")

        #--- Actions ---

        ac0l0, acol1, acol2 = st.columns([0.15,0.7, 0.15])
        with acol1:
            st.subheader("Actions:")
            st.markdown("- I have meet and introduced myself to all team members")
            st.markdown("- I have attended my first team meeting")

        with acol2:
            st.subheader(" ")
            st.checkbox("Done", key=684864)
            st.checkbox("Done", key=54654)

        # --- Status / Buttons ---
        st.markdown("")
        st.markdown("")
        margin, status, back, complete = st.columns([0.15, 0.6, 0.1, 0.15])
        with status:

            st.markdown("**Time to complete module:** 5 Days - You are on track!")

        with back:
            st.button("Back", key=654564)

        with complete:
            st.button("Complete", key=987897)
