import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Starbucks", page_icon="☕")

# Sidebar Navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Extras"])

# Data Preparation
uploaded_file = st.sidebar.file_uploader("Upload your Starbucks Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.sidebar.error("Error: Unable to read the uploaded file. Please upload a valid Excel file.")
else:
    df = pd.DataFrame({
        'Beverage': ['Coffee', 'Coffee', 'Tea', 'Juice'],
        'Size': ['Short', 'Tall', 'Grande', 'Venti'],
        'Calories': [5, 150, 120, 200],
        'Caffeine': [80, 150, 95, 0],
        'Category': ['Hot', 'Hot', 'Hot', 'Cold']
    })

# Home Page
if page == "Home":
    st.title("Starbucks Dataset Explorer ☕")
    st.image("https://upload.wikimedia.org/wikipedia/en/d/d3/Starbucks_Corporation_Logo_2011.svg", width=200)
    st.subheader("Welcome!")
    st.write(
        """
        Explore Starbucks data, visualize relationships, and generate insights with ease!
        Use the sidebar to navigate between pages.
        """
    )

# Data Overview Page
if page == "Data Overview":
    st.title("Data Overview")
    st.subheader("About the Dataset")
    st.write(
        """
        This dataset includes nutritional information for Starbucks beverages. You can view details like:
        - Beverage Size
        - Calories
        - Caffeine
        - Beverage Categories
        """
    )
    st.write("### Preview of the Dataset:")
    st.dataframe(df)
    st.write("### Summary Statistics:")
    st.write(df.describe())

# Exploratory Data Analysis (EDA)
if page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis 📊")

    # Numeric and Categorical Columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    obj_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Select Visualization Type
    st.subheader("Select a Visualization:")
    eda_type = st.multiselect("Choose visualization(s):", ["Histogram", "Box Plot",  "Bar Plot"])

    # Histogram
    if "Histogram" in eda_type:
        st.subheader("Histogram")
        selected_col = st.selectbox("Select a numerical column:", num_cols)
        if selected_col:
            st.plotly_chart(px.histogram(df, x=selected_col, title=f"Histogram of {selected_col}", color='Beverage'))

    # Box Plot
    if "Box Plot" in eda_type:
        st.subheader("Box Plot")
        y_col = st.selectbox("Select a column for Box Plot (y-axis):", num_cols)
        x_col = st.selectbox("Select a column for Box Plot (x-axis):", obj_cols)
        if y_col and x_col:
            st.plotly_chart(px.box(df, x=x_col, y=y_col, title=f"Box Plot: {y_col} vs {x_col}", color=x_col))

   
    # Bar Plot
    if "Bar Plot" in eda_type:
        st.subheader("Bar Plot")
        x_col = st.selectbox("Select x-axis (categorical):", obj_cols, key="bar_x")
        y_col = st.selectbox("Select y-axis (numerical):", num_cols, key="bar_y")
        if x_col and y_col:
            st.plotly_chart(px.bar(df, x=x_col, y=y_col, title=f"Bar Plot: {y_col} by {x_col}", color=x_col))

# Extras Page
if page == "Extras":
    st.title("Secret Menu")

    st.subheader("Upload and Display an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

    st.subheader("Welcome!")
    st.write(
        """
         Starbucks Secret Menu Drinks that are Perfect for Valentine’s Day!

         Here’s the recipe:

              Double Chocolate Chip Frappuccino
              Made with white mocha instead of regular mocha
              Add raspberry syrup (2 pumps tall, 3 grande, 4 venti)

      st.subheader("Watch a YouTube Video")
    st.video("https://www.youtube.com/watch?v=dQpXtnaaYdk")         
        """
    )

    import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

if page == "Model Training and Evaluation":
    st.title("🛠️ Model Training and Evaluation")
