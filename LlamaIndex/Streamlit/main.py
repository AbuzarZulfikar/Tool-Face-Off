import streamlit as st

from streamlit_option_menu import option_menu


import home, analysis, account, history, about
st.set_page_config(
        page_title="OFIN",
)

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: dark;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:    
            app = option_menu(
                menu_title='OFIN',
                options=['Home','Account','Analysis','History','about'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#1F2B3E'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#1F3A5F"},
        "nav-link-selected": {"background-color": "#374357"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "Analysis":
            analysis.app()        
        if app == 'History':
            history.app()
        if app == 'about':
            about.app()    
             
          
             
    run()            
         
