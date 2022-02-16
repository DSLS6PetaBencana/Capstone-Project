#app.py
import app1
import app2
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title = 'Peta Bencana',
    page_icon = Image.open("Images/logoPetaBencanaID.png"),
    layout = 'wide'
)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
    
PAGES = {
    "MainDashboard": app1,
    "FloodDashboard": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox(
    'Pages',
    list(PAGES.keys()))

# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()