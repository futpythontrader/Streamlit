import streamlit as st
from login import show_login_page
from tela1 import show_tela1
# Importe as outras telas aqui

# Inicializando a sessão para armazenar o estado do usuário
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Mostrando a tela de login se o usuário não estiver logado
if not st.session_state['logged_in']:
    st.session_state['logged_in'] = show_login_page()
else:
    # Aqui você pode adicionar um menu ou botões para navegar entre as telas
    # Por exemplo:
    page = st.selectbox("Escolha sua tela", ["Tela 1", "Tela 2"])
    
    if page == "Tela 1":
        show_tela1()
    elif page == "Tela 2":
        show_tela2()
    # Adicione mais condições conforme necessário para suas outras telas
