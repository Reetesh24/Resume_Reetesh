import streamlit as st
st.header("MY PROJECTS")
img1 = "./Assests/Where Love Begins.jpg"
img2 = "./Assests/Night Full Of Mystery.png"
img3 = "./Assests/Broken.png"
img4 = "./Assests/I Wish I Could Tell Her Main file.png"
img5 = "./Assests/Wish We HAd Never Met Each Other.jpg"

st.markdown("#### Photoshop Work")
col1, col2, col3 = st.columns([1,1,1])
with col1:
    with st.expander("Where Love Begins"):
        st.image(img1)
with col2:
    with st.expander("Night Full Of Mystery"):
        st.image(img2)
with col3:
    with st.expander("Broken"):
        st.image(img3)

col4,col5, col6 = st.columns([1,1,1])
with col4:
    with st.expander("I Wish I Could Tell Her"):
        st.image(img4)
with col5:
    with st.expander("Wish We Had Never Met Each Other"):
        st.image(img5)

st.markdown("#### Streamlit Project")
with st.container(border=True):
    st.markdown("**Portfolio:** [_Click Here_](https://reetesh-portfolio.streamlit.app/)")
    st.markdown("**To-Do List:** [_Click Here_](https://my-personal-todo.streamlit.app/)")