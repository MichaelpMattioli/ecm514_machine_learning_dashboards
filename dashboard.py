import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="NBA Dashboard", 
                   page_icon=":bar_chart:",
                   layout="wide"
)

df = pd.read_csv("basquete.csv")

st.sidebar.header("Selecione seu filtro aqui:")
season = st.sidebar.multiselect(
    "selecione a temporada:",
    options=df['season'].unique(),
    default=df['season'].unique(),
)

team = st.sidebar.selectbox(
    "selecione o time da casa:",
    options=df['team'].unique()
)

df_selection = df.query(
    "season == @season & team == @team"
)

# st.dataframe(df_selection)

st.title(":bar_chart: Resumo de jogos ganhos por time e temporada da NBA")
st.markdown("##")

total_jogos_ganhos = int(df_selection['won'].sum())

total_jogos_perdidos = int(df_selection['won'].count() - df_selection['won'].sum())

total_jogos = int(df_selection['won'].count())


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total de jogos ganhos")
    st.subheader(f"{total_jogos_ganhos}")
with middle_column:
    st.subheader("Total de jogos perdidos")
    st.subheader(f"{total_jogos_perdidos}")
with right_column:
    st.subheader("Total de jogos")
    st.subheader(f"{total_jogos}")
    
st.markdown("---")


df_distribuicao = df_selection.groupby(by=["season", "won"]).size().reset_index(name="counts")

df_distribuicao['won'] = df_distribuicao['won'].replace([True,False], ['Ganhou','Perdeu'])

fig = px.bar(data_frame=df_distribuicao, x="season", y="counts",color="won", barmode="group")

st.plotly_chart(fig)
    