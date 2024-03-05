import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('day_clean.csv')
df['dteday'] = pd.to_datetime(df['dteday'])



st.title('Dashboard Bike Sharing')

def sidebar(df):

    min_date = df['dteday'].min()
    max_date = df['dteday'].max()

    def on_change():
        st.session_state.date = date

    # Mengambil start_date & end_date dari date_input
    date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
        on_change=on_change
        )

    return date

def season(df):

    fig ,ax = plt.subplots(figsize = (20,10))
    sns.barplot(data = df , x= 'season', y = 'cnt')

    st.pyplot(fig)

def months(df):

    fig1 ,ax1 = plt.subplots(figsize = (20,10))
    sns.barplot(data = df , x= 'mnth', y = 'cnt')
    st.pyplot(fig1)

def temp(df):
    fig2 ,ax2 = plt.subplots(figsize = (10,10))
    sns.regplot(x=df["temp"], y=df["cnt"])
    plt.xlabel("Temp")
    plt.ylabel("Casual and Registered")
    st.pyplot(fig2)

def atemp(df):
   fig3 ,ax3 = plt.subplots(figsize = (10,10))
   sns.regplot(x=df["atemp"], y=df["cnt"])
   plt.xlabel("atemp")
   plt.ylabel("Casual and Registered")
   st.pyplot(fig3)

def hum(df):
    fig4 ,ax4 = plt.subplots(figsize = (10,10))
    sns.regplot(x=df["hum"], y=df["cnt"])
    plt.xlabel("Hum")
    plt.ylabel("Casual and Registered")
    st.pyplot(fig4)
def windspeed(df):
    fig5 ,ax5 = plt.subplots(figsize = (10,10))
    sns.regplot(x=df["windspeed"], y=df["cnt"])
    plt.xlabel("Wind Speed")
    plt.ylabel("Casual and Registered")
    st.pyplot(fig5)

col1, col2, col3 = st.columns(3)
 
with col1:
    date = sidebar(df)
    if(len(date) == 2):
        main_df = df[(df["dteday"] >= str(date[0])) & (df["dteday"] <= str(date[1]))]
    else:
        main_df = df[(df["dteday"] >= str(st.session_state.date[0])) & (df["dteday"] <= str(st.session_state.date[1]))]
    
 
with col2:
    total_penyewa = main_df['cnt'].sum()
    st.metric(label="Total Rental", value=total_penyewa)
    
with col3:
    total_record = main_df['instant'].count()
    st.metric(label="Total Record", value=total_record)
 

st.subheader('Count of bikes during different Season')
season(main_df)

st.subheader('Count of bikes during different months')
months(main_df)


st.subheader('Regression Count')
col1, col2 = st.columns(2)
 
with col1:
    temp(main_df)
     
with col2:
    atemp(main_df)

col1, col2 = st.columns(2)
 
with col1:
    hum(main_df)
with col2:
    windspeed(main_df)