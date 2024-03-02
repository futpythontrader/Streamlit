import streamlit as st
from usuarios import usuarios_permitidos

def show_login_page():
    st.title("Login")

    # Campos de entrada para o usuário e senha
    login = st.text_input("Login")
    senha = st.text_input("Senha", type="password")

    if st.button("Login"):
        # Verificando se as credenciais correspondem a algum usuário
        usuario_autenticado = any(user for user in usuarios_permitidos if user["login"] == login and user["senha"] == senha)
        
        if usuario_autenticado:
            return True
        else:
            st.error("Login ou senha incorretos.")
    
    return False
