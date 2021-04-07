import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from apps.dataset import load_data

def app():
    st.title('Graphes')
    st.write('Voici les 3 graphes qui concernent:')
    show_graph()

def show_graph():
    # Affichage des graphiques
    data1=load_data()
    fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Closing value']))

    fig.update_layout(
        title={
            'text': "La Valeur du Down Jones à la fermeture selon l'année",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in points']))

    fig.update_layout(
        title={
            'text': "Le nombre de points du Down Jones à l'année",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

    fig = go.Figure(data=go.Scatter(x=data1['Annee'], y=data1['Change in percent']))

    fig.update_layout(
        title={
            'text': "Le change en pourcentage du Down Jones à l'année",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

        