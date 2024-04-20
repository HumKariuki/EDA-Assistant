import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from PIL import Image
from io import BytesIO

# Disable warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

# Initialize session state
if 'clicked_button' not in st.session_state:
    st.session_state.clicked_button = False

# Function to update session state
def clicked():
    st.session_state.clicked_button = True

# Function to handle data analysis
def analyze_data(df):
    st.write("**Data Overview**")
    st.write("The first few rows of your dataset look like this:")
    st.write(df.head())  

    # Preprocessing of Data
    st.write("**Preprocessing of Data**" )

    # Check the shape of the dataset
    st.write("The shape of your dataset is:")
    st.write(df.shape) 

    # Check the columns of the dataset
    st.write("The columns of your dataset are:")
    st.write(df.columns)  

    # Check the datatypes of the dataset
    st.write("The datatypes of your dataset are:")
    st.write(df.dtypes)  

    # Check the missing values in the dataset
    st.write("The missing values in your dataset are:")
    st.write(df.isnull().sum())  

    # Allow users to select columns for further analysis
    selected_columns = st.multiselect("Select variables for further analysis:", df.columns)

    if not selected_columns:
        return

    # Categorical variable analysis
    st.subheader("Categorical Variable Analysis")
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    selected_categorical_columns = st.multiselect("Select categorical variables for analysis:", categorical_columns)

    if selected_categorical_columns:
        # Frequency bar graph
        for column in selected_categorical_columns:
            st.write(f"The frequency bar graph for {column}:")
            plt.figure(figsize=(10, 6))
            sns.countplot(x=column, data=df)
            plt.xticks(rotation=45)
            st.pyplot()

        # Multivariate analysis (if more than one categorical variable selected)
        if len(selected_categorical_columns) > 1:
            st.write("The multivariate analysis for selected categorical variables:")
            st.write(df[selected_categorical_columns].value_counts())

    # Continuous variable analysis
    st.subheader("Continuous Variable Analysis")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    selected_numeric_columns = st.multiselect("Select continuous variables for analysis:", numeric_columns)

    if selected_numeric_columns:
        # Descriptive statistics
        if st.checkbox("Display descriptive statistics for selected variables"):
            st.write("Summary Statistics for Selected Continuous Variables:")
            st.write(df[selected_numeric_columns].describe())

        # Histogram
        for column in selected_numeric_columns:
            st.write(f"The histogram for {column}:")
            plt.figure(figsize=(10, 6))
            plt.hist(df[column], bins='auto')
            plt.xlabel(column)
            plt.ylabel("Frequency")
            st.pyplot()

        # Box plot
        for column in selected_numeric_columns:
            st.write(f"The box plot for {column}:")
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=column, data=df)
            st.pyplot()

        # Regression analysis (if more than one continuous variable selected)
        if len(selected_numeric_columns) > 1:
            st.write("The regression analysis for selected continuous variables:")
            st.write(df[selected_numeric_columns].corr())

    # Additional analysis options
    st.subheader("Additional Analysis Options")

    # Scatter plot
    selected_scatter_columns = st.multiselect("Select variables for scatter plot analysis:", numeric_columns)
    if len(selected_scatter_columns) == 2:
        st.write("Scatter plot:")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=selected_scatter_columns[0], y=selected_scatter_columns[1], data=df)
        st.pyplot()

    # Correlation heatmap
    if st.checkbox("Display correlation heatmap"):
        st.write("Correlation heatmap:")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
        st.pyplot()

    # Pairplot
    if st.checkbox("Display pairplot"):
        st.write("Pairplot:")
        sns.pairplot(df[selected_numeric_columns])
        st.pyplot()

    # Distribution plot
    selected_dist_columns = st.multiselect("Select variables for distribution plot analysis:", numeric_columns)
    if selected_dist_columns:
        for column in selected_dist_columns:
            st.write(f"Distribution plot for {column}:")
            plt.figure(figsize=(10, 6))
            sns.histplot(df[column], kde=True)
            st.pyplot()

# Title 
st.title("🤖 AI Assistant for Data Science")

# Welcoming message 
st.write('**Hello!** I am your AI assistant and I am here to help with your data science projects.')
st.write('**Let\'s explore your data together!**')

# Explaination Sidebar
with st.sidebar:
    st.write('**Your Data Science Adventure Begins with a CSV file.**')
    st.caption('''You may already know that every exciting data science journey starts with a dataset.
            That's why I'd love for you to upload a CSV file. Once we have your data in hand, we'll
            dive into understanding it and have some fun exploring it. Then, we'll work together
            to shape your business challenges into a data science framework. I'll introduce you to 
            the coolest machine learning models, and we'll use them to tackle your problem. 
            Sounds fun, right?!''')
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", use_column_width=True)
    st.caption("<p style='text-align:center'>Designed and Developed by 🫱🏻‍🫲🏼: Japanjot Singh</p>", unsafe_allow_html=True)

# Button to initiate the process
if not st.session_state.clicked_button:
    if st.button("🚀 Let's get started", on_click=clicked):
        st.session_state.clicked_button = True

# Check if the button was clicked
if st.session_state.clicked_button:
    df = st.file_uploader('📁 Upload your CSV file here', type="csv")
    if df is not None:
        df = pd.read_csv(df)
        analyze_data(df)
