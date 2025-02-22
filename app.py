import streamlit as st

# Pages Setup

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page="views/Colour-Palatte-Generator.py",
    title="Color Palatte Generator",
    icon=":material/chat:",
)

# Navigation Setup

pg = st.navigation(
    {
        "info" : [about_page],
        "projects" : [project_1_page]
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made By Hamza Nasir.")



pg.run()