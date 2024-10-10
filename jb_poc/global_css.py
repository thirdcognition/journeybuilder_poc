import streamlit as st

#Hide image fullscreen, control page wirth

def init_css():

    st.markdown("""
            
            <style>
                    button[title="View fullscreen"]{
                    visibility: hidden;}
            </style>
            
            
            <style>
                   .block-container {
                        max-width: 1000px;  #control page width
                        padding-top: 1rem;
                        padding-bottom: 2rem;
                        padding-left: 1rem;
                        padding-right: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)