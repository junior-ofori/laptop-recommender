
# Explainable Laptop Recommender

An interactive, rule-based laptop recommendation system developed
for the Intelligent Interactive Systems module at the
University of Birmingham.

## Project Overview

The Explainable Laptop Recommender helps users explore
laptop options and understand the trade offs between them

Users can:
- Set a maximum budget
- Select their main priority: battery life, performance,
  or portability
- View laptops ranked according to their selected priority
- Choose two laptops to compare
- Receive explanations highlighting the differences and
  disadvantages of choosing one laptop over another
- Adjust their preferences and explore alternative options

## How It Works

The system uses a deterministic recommendation algorithm.

1. Laptops exceeding the user's budget are excluded
2. Eligible laptops are ranked by the selected priority
3. The user can select two eligible laptops for comparison
4. The system calculates differences in price, battery life,
   performance and weight
5. A priority-sensitive explanation identifies the stronger
   option for the selected attribute and its disadvantages
   relative to the alternative

The system does not use machine learning or a large
language model

## Technologies

- Python
- Streamlit
- Git and GitHub

## Limitations

- The system considers one priority at a time rather than
  calculating overall suitability across multiple needs
- The explanations are generated using predefined rules
- The system does not access live product information

## Installation and Running Instructions

### Requirements

- Python 3
- pip

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/junior-ofori/laptop-recommender.git
   ```

2. Navigate into the project folder:

   ```bash
   cd laptop-recommender
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install Streamlit:

   ```bash
   python -m pip install streamlit
   ```

6. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

The application will open in your web browser.

## Project Files

- `app.py` — Streamlit interface, recommendation logic,
  comparison functionality and explanations.
- `laptops.py` — Fictional laptop dataset.
- `README.md` — Project documentation.


## Testing

Six manual functional tests were carried out to verify
the recommendation and comparison functionality

| Test | Input / Action | Expected Result | Result |
|---|---|---|---|
| Budget filtering | £700 budget, Performance | Only Laptop A is eligible | Pass |
| Preference ranking | £900 budget, Battery life | Ranking: D, A, B | Pass |
| Trade-off accuracy | Compare B and D, Performance | Correct differences in price, battery and weight | Pass |
| Selection order | Reverse B and D | Same trade-off conclusions | Pass |
| Identical selections | Compare A with A | Warning displayed; no comparison generated | Pass |
| No matching laptops | £300 budget | Warning displayed; no recommendations or errors | Pass |

All six tests passed during manual testing.

### Testing Limitations

These tests verify specific functional behaviours
They do not establish that the system improves users'
understanding, satisfaction or decision quality

## Development History

The application was developed incrementally:

1. **Initial interface**
   - Created a Streamlit application with a budget slider
   - Verified that the interface responded to user input

2. **Recommendation functionality**
   - Added a fictional laptop dataset
   - Implemented budget filtering and preference-based ranking
   - Tested the ordering of eligible laptops

3. **Interactive comparison**
   - Added dropdowns allowing users to select two laptops
   - Implemented comparisons of price, battery life,
     performance and weight
   - Added feedback for identical laptop selections

4. **Trade-off explanations**
   - Added priority-sensitive comparison conclusions
   - Improved explanations to identify specific disadvantages
     of choosing one laptop over another

5. **Interface refinement and testing**
   - Simplified recommendation cards to reduce repetition
   - Added feedback for budgets with no matching laptops
   - Completed six manual functional tests

## Use of AI Assistance

ChatGPT was used to:

- Plan the application structure and interaction design
- Explaining Python and Streamlit functionality
- Suggesting debugging approaches
- Providing functional tests 
- Structuring the README documentation 

Documentation was checked against the application to check accuracy

## Future Improvements

Potential improvements include:

- Supporting multiple priorities simultaneously
- Allowing users to adjust the importance of different
  attributes
- Evaluating whether explanations improve users'
  understanding of product trade-offs
- Using verified product data instead of fictional examples
