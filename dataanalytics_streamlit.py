import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
batsman=pd.read_csv('https://raw.githubusercontent.com/akpythonyt/Datasets/main/Top_100_batsman.csv')
st.title('IPL analytics 2008- 2019')
st.title('Batsman KPIs')
Batsman_matches = batsman[batsman['Runs']>3000]
topfive=(Batsman_matches['PLAYER'].iloc[0:5])
df = batsman
fig5 = px.bar(df, x=batsman['PLAYER'], y=batsman['Avg'], color=batsman['SR'])
st.plotly_chart(fig5)
st.title('Top 5 batsman based on runs')
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=topfive, y=(batsman['Runs'].iloc[0:5]),
                    mode='lines+markers',
                    name='lines+markers'))
st.plotly_chart(fig6)

Matches=pd.read_csv('https://raw.githubusercontent.com/akpythonyt/Datasets/main/matches.csv')
bat=Matches['toss_winner'].loc[Matches['toss_decision']=='bat']
battoss=(bat.value_counts())
st.title('Teams chose batting when they won toss')
data = bat
fig7 = px.bar(data, x=battoss.values, y=battoss.index)
st.plotly_chart(fig7)
field=Matches['toss_winner'].loc[Matches['toss_decision']=='field']
fieldtoss=(field.value_counts())
data = field
st.title('Teams chose bowling when they won toss')
fig8 = px.bar(data, x=fieldtoss.values, y=fieldtoss.index)
st.plotly_chart(fig8)
st.title('Overall toss mapping')
Overalltosswin=fieldtoss+battoss
pie_col = ["Red","Blue","Yellow","Purple","Black","Indigo","Salmon","Olive","Green","Teal","Aqua","Silver","Navy",'white']
fig9 = px.pie(values=Overalltosswin.values, names= Overalltosswin.index)
st.plotly_chart(fig9)
count = Matches['winner'].value_counts()
st.title('Most successful teams based on win count')
pie_col = ["Red","Blue","Yellow","Purple","Black","Indigo","Salmon","Olive","Green","Teal","Aqua","Silver","Navy",'white']
fig = px.pie(values=count.values, names= count.index)
st.plotly_chart(fig)
st.title('Player of the Match award')
count = Matches['player_of_match'].value_counts()
fig1 = go.Figure(data=[go.Scatter(
    x=count.index, y=count.head(5),
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)','yellow'],
        opacity=[1, 0.8, 0.6, 0.4,0.3],
        size=[40, 60, 80, 100,105],
    )
)])
st.plotly_chart(fig1)
st.title('Top 5 Bowlers Based on wickets')
Bowlers=pd.read_csv('https://raw.githubusercontent.com/akpythonyt/Datasets/main/Top_100_bowlers.csv')
Bowlers_matches = Bowlers[Bowlers['Wkts']>1]
topfive=(Bowlers_matches['PLAYER'].iloc[0:5])
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=topfive, y=(Bowlers['Wkts'].iloc[0:5]),
                    mode='lines+markers',
                    name='lines+markers'))
st.plotly_chart(fig2)

st.title('Bowlers KPI')
df = Bowlers

fig3 = px.bar(df, x=Bowlers['PLAYER'], y=Bowlers['Econ'], color=Bowlers['Wkts'])
st.plotly_chart(fig3)
st.title('Bowers who leaking more runs')
Bowlers_matches = Bowlers[Bowlers['Econ']>=8.50]
Ecobowlers=(Bowlers_matches['PLAYER'])
Economy=Bowlers_matches['Econ']
fig4 = px.pie(values=Economy, names= Ecobowlers)

st.plotly_chart(fig4)
