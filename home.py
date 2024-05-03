import streamlit as st

def home():
    st.image("assets/bg1.gif", use_column_width=True)
    st.title("Welcome to OFIN: AI-Powered Financial Analysis")
    st.write("OFIN is an AI-based application that utilizes advanced ML techniques to identify businesses' financial health.")
    st.write("It offers different types of analysis such as Horizontal, Vertical, and Ratio analysis.")
    st.write("Experience the power of OFIN by exploring the analysis options in the sidebar.")

def app():
    st.markdown("""
    <style>
    .reportview-container {
        background: url("assets/bg1.gif");
        background-size: cover;
    }
    .sidebar .sidebar-content {
        background-color: transparent;
    }
    .Widget>label {
        color: white;
    }
    .stButton>button {
        color: black;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    home()
