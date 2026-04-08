"""
🌸 Interactive Iris Dashboard

An interactive data exploration dashboard for the Iris dataset, built with Streamlit.

---

FEATURES:

- Filter by species (multi-select)
- Filter by Sepal Length, Sepal Width, Petal Length, and Petal Width using sliders
- Display filtered data in a table
- Download filtered data as CSV
- Scatter plots:
    - Sepal Length vs Sepal Width
    - Petal Length vs Petal Width
- Bar chart showing the count of each species in the filtered data

---

INSTALLATION & RUNNING:

1. Ensure Python >= 3.8 is installed.
2. Install dependencies:

    pip install streamlit pandas seaborn matplotlib

3. Run the dashboard:

    streamlit run dashboard.py

This will open your default web browser with the interactive dashboard.

DATASET:

- Iris dataset from the Seaborn library
- Columns: sepal_length, sepal_width, petal_length, petal_width, species
- Source: https://github.com/mwaskom/seaborn-data

AUTHOR:

Peter Kimutai Maiyo
