import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("🌸 Interactive Iris Dashboard")

st.markdown("""
This dashboard allows you to explore the Iris dataset interactively.
You can filter by species and numeric ranges, visualize relationships
between Sepal and Petal dimensions, and download the filtered data.
""")

# -----------------------------
# Load Dataset (with caching)
# -----------------------------
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    return pd.read_csv(url)

df = load_data()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔍 Filters")

species = st.sidebar.multiselect(
    "Select Species", options=df['species'].unique(), default=df['species'].unique()
)

sepal_length_range = st.sidebar.slider(
    "Sepal Length Range",
    float(df['sepal_length'].min()), float(df['sepal_length'].max()),
    (float(df['sepal_length'].min()), float(df['sepal_length'].max()))
)

sepal_width_range = st.sidebar.slider(
    "Sepal Width Range",
    float(df['sepal_width'].min()), float(df['sepal_width'].max()),
    (float(df['sepal_width'].min()), float(df['sepal_width'].max()))
)

petal_length_range = st.sidebar.slider(
    "Petal Length Range",
    float(df['petal_length'].min()), float(df['petal_length'].max()),
    (float(df['petal_length'].min()), float(df['petal_length'].max()))
)

petal_width_range = st.sidebar.slider(
    "Petal Width Range",
    float(df['petal_width'].min()), float(df['petal_width'].max()),
    (float(df['petal_width'].min()), float(df['petal_width'].max()))
)

# -----------------------------
# Filter the Data
# -----------------------------
filtered_data = df[
    (df['species'].isin(species)) &
    (df['sepal_length'] >= sepal_length_range[0]) & (df['sepal_length'] <= sepal_length_range[1]) &
    (df['sepal_width'] >= sepal_width_range[0]) & (df['sepal_width'] <= sepal_width_range[1]) &
    (df['petal_length'] >= petal_length_range[0]) & (df['petal_length'] <= petal_length_range[1]) &
    (df['petal_width'] >= petal_width_range[0]) & (df['petal_width'] <= petal_width_range[1])
]

# -----------------------------
# Display Filtered Data
# -----------------------------
st.subheader("📊 Filtered Data")
st.dataframe(filtered_data)

# -----------------------------
# Download Button
# -----------------------------
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(filtered_data)

st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv_data,
    file_name='filtered_iris_data.csv',
    mime='text/csv'
)

# -----------------------------
# Visualizations
# -----------------------------
st.subheader("🌼 Sepal Dimensions")
fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_data,
    x="sepal_length",
    y="sepal_width",
    hue="species",
    palette="Set2",
    s=100,
    ax=ax
)
ax.set_title("Sepal Length vs Sepal Width")
st.pyplot(fig)

st.subheader("🌸 Petal Dimensions")
fig2, ax2 = plt.subplots()
sns.scatterplot(
    data=filtered_data,
    x="petal_length",
    y="petal_width",
    hue="species",
    palette="Set1",
    s=100,
    ax=ax2
)
ax2.set_title("Petal Length vs Petal Width")
st.pyplot(fig2)

st.subheader("📈 Species Count")
species_count = filtered_data['species'].value_counts()
st.bar_chart(species_count)