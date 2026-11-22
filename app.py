import streamlit as st
from laptops import laptops

st.title("Explainable Laptop Recommender")

st.write("Find a laptop that matches your needs and understand the trade-offs.")

budget = st.slider(
    "What is your maximum budget (£)?",
    min_value=300,
    max_value=2000,
    value=900,
    step=50
)


priority = st.selectbox(
    "What matters most to you?",
    ["Battery life", "Performance", "Portability"]
)


eligible_laptops = []

for laptop in laptops:
    if laptop["price"] <= budget:
        eligible_laptops.append(laptop)

if priority == "Battery life":
    eligible_laptops.sort(
        key=lambda laptop: laptop["battery"],
        reverse=True
    )

elif priority == "Performance":
    eligible_laptops.sort(
        key=lambda laptop: laptop["performance"],
        reverse=True
    )

elif priority == "Portability":
    eligible_laptops.sort(
        key=lambda laptop: laptop["weight"]
    )

st.subheader("Recommended laptops")

st.caption(
    f"Showing laptops within your £{budget} budget, "
    f"ranked by {priority.lower()}."
)

for laptop in eligible_laptops:
    st.write(f"{laptop['name']} - £{laptop['price']}")


st.write(f"Your main priority is {priority}")

st.write(f"Your maximum budget is £{budget}")
