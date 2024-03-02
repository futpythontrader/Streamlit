import streamlit as st
import pandas as pd

def show_tela1():
    st.title("Tela 1")
    st.write("Bem-vindo à Tela 1!")

    def drop_reset_index(df):
        df = df.dropna()
        df = df.reset_index(drop=True)
        df.index += 1
        return df

    # Função para ler e processar o CSV
    def load_data(url):
        # Ler o arquivo CSV
        df = pd.read_csv(url, usecols=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'B365H', 'B365D', 'B365A', 'B365>2.5', 'B365<2.5'])
        
        # Renomear colunas
        df.columns = ['Home', 'Away', 'Goals_H', 'Goals_A', 'Odd_H', 'Odd_D', 'Odd_A', 'Odd_Over', 'Odd_Under']
        return df

    # Função para filtrar o DataFrame
    def filter_data(df, odd_min, odd_max):
        # Aplicar filtros para cada tipo de odd
        filtered_df = df[
            (df['Odd_Over'] >= odd_min) & (df['Odd_Over'] <= odd_max) 
        ]
        return filtered_df

    # Carregar os dados
    url = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"
    df = load_data(url)

    # Interface do usuário no Streamlit
    st.title("Análise de Dados do Futebol")

    # Inputs para os filtros de odds na área principal
    odd_min, odd_max = st.columns(2)
    with odd_min:
        odd_min_value = st.number_input('Odd Mínima', value=float(df[['Odd_Over']].min().min()), step=0.1)
    with odd_max:
        odd_max_value = st.number_input('Odd Máxima', value=float(df[['Odd_Over']].max().max()), step=0.1)

    # Botão para aplicar filtros
    if st.button('Filtrar Dados'):
        filtered_df = filter_data(df, odd_min_value, odd_max_value)
        filtered_df = drop_reset_index(filtered_df)
        st.dataframe(filtered_df)
    else:
        df = drop_reset_index(df)
        st.dataframe(df)

