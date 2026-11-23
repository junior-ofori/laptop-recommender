import streamlit as st
from laptops import laptops


def explain_recommendation(laptop, priority):
    if priority == "Battery life":
        return (
            f"This laptop provides {laptop['battery']} hours "
            f"of battery life."
        )

    elif priority == "Performance":
        return (
            f"This laptop has a performance score of "
            f"{laptop['performance']}/10."
        )

    elif priority == "Portability":
        return (
            f"This laptop weighs {laptop['weight']} kg."
        )


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

#recommendations

if not eligible_laptops:
    st.warning(
        "No laptops match your budget. "
        "Try increasing your maximum budget."
    )

for position, laptop in enumerate(eligible_laptops, start=1):
    st.markdown(f"### {position}. {laptop['name']}")
    st.write(f"Price: £{laptop['price']}")

    explanation = explain_recommendation(laptop, priority)
    st.info(explanation)

    st.divider()




st.subheader("Understand the trade-offs")

st.write(
    "Choose two laptops to see what you gain "
    "and what you give up."
)

if len(eligible_laptops) >= 2:
    laptop_names = [
        laptop["name"] for laptop in eligible_laptops
    ]

    first_choice = st.selectbox(
        "First laptop",
        laptop_names,
        key="first_laptop"
    )

    second_choice = st.selectbox(
        "Second laptop",
        laptop_names,
        index=1,
        key="second_laptop"
    )

    first_laptop = next(
        laptop for laptop in eligible_laptops
        if laptop["name"] == first_choice
    )

    second_laptop = next(
        laptop for laptop in eligible_laptops
        if laptop["name"] == second_choice
    )

    if first_choice == second_choice:
        st.warning("Please select two different laptops.")
    else:
        st.write(
            f"Comparing {first_laptop['name']} "
            f"with {second_laptop['name']}"
        )

        price_difference = abs(
            first_laptop["price"] - second_laptop["price"]
        )

        battery_difference = abs(
            first_laptop["battery"] - second_laptop["battery"]
        )

        if first_laptop["price"] < second_laptop["price"]:
            st.write(
                f"{first_choice} is £{price_difference} cheaper "
                f"than {second_choice}."
            )
        elif first_laptop["price"] > second_laptop["price"]:
            st.write(
                f"{second_choice} is £{price_difference} cheaper "
                f"than {first_choice}."
            )
        else:
            st.write("Both laptops have the same price.")

        if first_laptop["battery"] > second_laptop["battery"]:
            st.write(
                f"{first_choice} offers {battery_difference} "
                f"more hours of battery life."
            )
        elif first_laptop["battery"] < second_laptop["battery"]:
            st.write(
                f"{second_choice} offers {battery_difference} "
                f"more hours of battery life."
            )
        else:
            st.write("Both laptops have the same battery life.")

        performance_difference = abs(
            first_laptop["performance"] - second_laptop["performance"]
        )

        weight_difference = round(
            abs(first_laptop["weight"] - second_laptop["weight"]), 2
        )

        if first_laptop["performance"] > second_laptop["performance"]:
            st.write(
                f"{first_choice} has a performance score "
                f"{performance_difference} points higher than {second_choice}."
            )
        elif first_laptop["performance"] < second_laptop["performance"]:
            st.write(
                f"{second_choice} has a performance score "
                f"{performance_difference} points higher than {first_choice}."
            )
        else:
            st.write("Both laptops have the same performance score.")

        if first_laptop["weight"] < second_laptop["weight"]:
            st.write(
                f"{first_choice} is {weight_difference} kg lighter "
                f"than {second_choice}."
            )
        elif first_laptop["weight"] > second_laptop["weight"]:
            st.write(
                f"{second_choice} is {weight_difference} kg lighter "
                f"than {first_choice}."
            )
        else:
            st.write("Both laptops have the same weight.")

        st.subheader("What does this mean for your decision?")

        if priority == "Performance":
            attribute = "performance"
            higher_is_better = True

        elif priority == "Battery life":
            attribute = "battery"
            higher_is_better = True

        else:
            attribute = "weight"
            higher_is_better = False

        first_value = first_laptop[attribute]
        second_value = second_laptop[attribute]

        if first_value == second_value:
            st.info(
                f"Both laptops are equally ranked for {priority.lower()}. "
                "Consider their other differences before deciding."
            )

        else:
            if higher_is_better:
                first_is_better = first_value > second_value
            else:
                first_is_better = first_value < second_value

            if first_is_better:
                preferred = first_laptop
                alternative = second_laptop
            else:
                preferred = second_laptop
                alternative = first_laptop

            
            trade_offs = []

            if preferred["price"] > alternative["price"]:
                difference = preferred["price"] - alternative["price"]
                trade_offs.append(f"costing £{difference} more")

            if preferred["battery"] < alternative["battery"]:
                difference = alternative["battery"] - preferred["battery"]
                trade_offs.append(
                    f"providing {difference} fewer hours of battery life"
                )

            if preferred["performance"] < alternative["performance"]:
                difference = alternative["performance"] - preferred["performance"]
                trade_offs.append(
                    f"having a performance score {difference} points lower"
                )

            if preferred["weight"] > alternative["weight"]:
                difference = round(
                    preferred["weight"] - alternative["weight"], 2
                )
                trade_offs.append(f"weighing {difference} kg more")

            if trade_offs:
                trade_off_text = ", ".join(trade_offs)

                st.info(
                    f"Based on your priority of {priority.lower()}, "
                    f"{preferred['name']} is the stronger option. "
                    f"However, choosing it over {alternative['name']} "
                    f"means {trade_off_text}."
                )
            else:
                st.info(
                    f"Based on your priority of {priority.lower()}, "
                    f"{preferred['name']} is the stronger option "
                    "and has no disadvantages across the other "
                    "attributes in this dataset."
                )





else:
    st.info("At least two laptops within budget are needed for comparison.")



#st.write(f"Your main priority is {priority}")

#st.write(f"Your maximum budget is £{budget}")
