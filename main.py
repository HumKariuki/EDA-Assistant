import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize session state
if 'selected_columns' not in st.session_state:
    st.session_state.selected_columns = {}

# Function to update session state
def update_selected_columns(step, selected_columns):
    st.session_state.selected_columns[step] = selected_columns

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

    # Allow users to select variables for each analysis step
    selected_columns_summary_stats = st.multiselect("Select variables for Summary Statistics:", df.columns)
    update_selected_columns("Summary Statistics", selected_columns_summary_stats)

    selected_columns_skewness = st.multiselect("Select variables for Skewness Analysis:", df.columns)
    update_selected_columns("Skewness Analysis", selected_columns_skewness)

    selected_columns_kurtosis = st.multiselect("Select variables for Kurtosis Analysis:", df.columns)
    update_selected_columns("Kurtosis Analysis", selected_columns_kurtosis)

    selected_columns_line_chart = st.multiselect("Select variables for Line Chart:", df.columns)
    update_selected_columns("Line Chart", selected_columns_line_chart)

    selected_columns_categorical = st.multiselect("Select categorical variables for analysis:", df.select_dtypes(include='object').columns)
    update_selected_columns("Categorical Analysis", selected_columns_categorical)

    selected_columns_continuous = st.multiselect("Select continuous variables for analysis:", df.select_dtypes(exclude='object').columns)
    update_selected_columns("Continuous Analysis", selected_columns_continuous)

    # Perform analysis based on selected columns
    if selected_columns_summary_stats:
        st.write("Summary Statistics for Selected Variables:")
        st.write(df[selected_columns_summary_stats].describe())

    if selected_columns_skewness:
        st.write("The skewness values for selected variables are:")
        st.write(df[selected_columns_skewness].skew())

    if selected_columns_kurtosis:
        st.write("The kurtosis values for selected variables are:")
        st.write(df[selected_columns_kurtosis].kurt())

    if selected_columns_line_chart:
        for column in selected_columns_line_chart:
            st.write(f"The line chart for {column}:")
            st.line_chart(df[column])

    if selected_columns_categorical:
        st.write("Categorical Data Analysis:")
        for column in selected_columns_categorical:
            st.write(f"Frequency bar graph for {column}:")
            plt.figure(figsize=(8, 6))
            sns.countplot(x=column, data=df)
            st.pyplot()

            st.write(f"Multivariate analysis for {column} with target variable:")
            target_variable = st.selectbox("Select target variable:", df.columns)
            if target_variable != column:
                plt.figure(figsize=(8, 6))
                sns.countplot(x=column, hue=target_variable, data=df)
                st.pyplot()

    if selected_columns_continuous:
        st.write("Continuous Data Analysis:")
        for column in selected_columns_continuous:
            st.write(f"Descriptive statistics for {column}:")
            st.write(df[column].describe())

            st.write(f"Histogram for {column}:")
            plt.figure(figsize=(8, 6))
            sns.histplot(df[column], kde=True)
            st.pyplot()

            st.write(f"Box plot for {column}:")
            plt.figure(figsize=(8, 6))
            sns.boxplot(y=df[column])
            st.pyplot()

            st.write(f"Regression analysis for {column}:")
            target_variable = st.selectbox("Select target variable:", df.columns)
            if target_variable != column:
                plt.figure(figsize=(8, 6))
                sns.regplot(x=column, y=target_variable, data=df)
                st.pyplot()

# Title 
st.title("AI Assistant for Data Science 🤖")

# Welcoming message 
st.write('Hello,👋🏼 I am your AI assistant and I am here to help with your data science projects.')

# Explaination Sidebar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with a CSV file.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset.
            That's why I'd love for you to upload a CSV file. Once we have your data in hand, we'll
            dive into understanding it and have some fun exploring it. Then, we'll work together
            to shape your business challenges into a data science framework. I'll introduce you to 
            the coolest machine learning models, and we'll use them to tackle your problem. 
            Sounds fun, right?!**''')
    
    # Divider to create a line between the two sections
    st.divider()
    
    # Caption to add text in the center
    st.caption("<p style='text-align:center'>Designed and Developed by 🫱🏻‍🫲🏼: Japanjot Singh</p>", unsafe_allow_html=True)

# Button to initiate the process
if st.button("Let's get started"):
    df = st.file_uploader('Upload your CSV file here', type="csv")
    if df is not None:
        df = pd.read_csv(df)
        analyze_data(df)
