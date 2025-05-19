import streamlit as st
st.set_page_config(page_title= "Resume")

about_page = st.Page(page= "Pages/About_Me.py",
                     title= "About Me",
                     icon= ":material/account_circle:",
                     default= True)

contact_page = st.Page(page='Pages/Contact_Me.py',
                       title= 'Contact Me',
                       icon= ':material/call:')

hobbies = st.Page(page='Pages/hobbies.py',
                  title="Hobbies",
                  icon=':material/interests:')

projects = st.Page(page= 'Pages/projects.py',
                   title= "Projects",
                   icon=':material/work:')

# pg = st.navigation(pages=[about_page, contact_page, hobbies])

pg = st.navigation({
    "Info" : [about_page],
    "Contact" : [contact_page],
    "Interest Section" : [hobbies, projects]
})

st.sidebar.text("Made with Python and Streamlit")
pg.run()
