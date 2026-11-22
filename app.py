import streamlit as st

st.title("Explainable Laptop Recommender")

st.write("Find a laptop that matches your needs and understand the trade-offs.")

budget = st.slider(
    "What is your maximum budget (£)?",
    min_value=300,
    max_value=2000,
    value=900,
    step=50
)

st.write(f"Your maximum budget is £{budget}")
