import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title('Data')
    st.write("Le dataframe de la dataset Dow_Jones ")
    df = load_data()
    st.dataframe(df)



@st.cache
def load_data():
    df = pd.read_csv("./apps/data/trade5.csv",index_col=0)
    return df




