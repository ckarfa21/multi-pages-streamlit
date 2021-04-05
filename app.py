import streamlit as st
from multiapp import MultiApp
from apps import home, dataset,graph # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data ", dataset.app)
app.add_app("Graphe",graph.app)

# The main app
app.run()