import streamlit as st

def show_login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "admin":
            return True
        else:
            st.error("Incorrect username or password.")
    return False
