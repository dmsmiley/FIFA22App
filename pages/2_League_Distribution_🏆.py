import streamlit as st
import plotly.express as px
import pandas as pd

data_file = 'fifa22data.csv'
df = pd.read_csv(data_file, index_col=["FullName"])

potential_stats = ['Age', 'Height', 'Weight', 'Overall', 'Potential', 'Growth', 'TotalStats',
                    'BaseStats', 'ValueEUR', 'WageEUR', 'ReleaseClause', 'IntReputation',
                    'WeakFoot', 'SkillMoves', 'PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
                    'DefendingTotal', 'PhysicalityTotal', 'Crossing', 'Finishing', 'HeadingAccuracy',
                    'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
                    'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility',
                    'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                    'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
                    'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle',
                    'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes',
                    'STRating', 'LWRating', 'LFRating', 'CFRating', 'RFRating', 'RWRating',
                    'CAMRating', 'LMRating', 'CMRating', 'RMRating', 'LWBRating',
                    'CDMRating', 'RWBRating', 'LBRating', 'CBRating', 'RBRating','GKRating']

unique_leagues = list(set([x for x in df['Club League'] if pd.isnull(x) == False]))

league = st.selectbox('Type League: ', 
                      options=unique_leagues,
                      index = unique_leagues.index("English Premier League") if "English Premier League" in unique_leagues else -1)

stat = st.selectbox('Stat:', options=potential_stats)

newer_df = df[df.isin([league]).any(axis=1)]

#Boxplot

fig = px.box(newer_df,
                y=stat,
                x='Club')

st.plotly_chart(fig)

#Expander One
expander1 = st.expander(label= f'Player {stat} by Club in {league}')

with expander1:
    clubs = st.selectbox("Club:", options=list(set([x for x in newer_df['Club'] if pd.isnull(x) == False])))

    expander1_df = df[df.isin([clubs]).any(axis=1)].sort_values(by=[stat], ascending=False)[stat]
    logo_df = df[df.isin([clubs]).any(axis=1)]['Club Logo'][0]

    st.image(logo_df)
    st.dataframe(expander1_df)


#Expander Two
expander2 = st.expander(label='Compare Clubs in Different Leagues')

with expander2:
    clubs = st.multiselect("Club:", options=list(set([x for x in df['Club'] if pd.isnull(x) == False])))
    ex_stat = st.selectbox('Stat:  ', options=potential_stats)

    ex_club_df = df[df['Club'].isin(clubs)]

    fig = px.box(ex_club_df,
                    y = ex_stat,
                    x ='Club')

    st.plotly_chart(fig)
