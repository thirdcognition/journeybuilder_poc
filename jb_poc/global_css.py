import streamlit as st


#Hide image fullscreen, control page wirth, adjust typeface

def init_css():
    with open("style.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    st.markdown("""
            
            
            
            <style>
                    button[title="View fullscreen"]{
                    visibility: hidden;}
            </style>
            
            
            
            <style>
                   .block-container {
                        max-width: 1000px;  #control page width
                        padding-top: 0rem;
                        padding-bottom: 2rem;
                        padding-left: 1rem;
                        padding-right: 1rem;
                    }
                
                    
            </style>
            """, unsafe_allow_html=True)