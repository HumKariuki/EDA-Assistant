import streamlit as st
import pandas as pd

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

    # Check if any columns are selected
    if selected_columns:
        # Display summary statistics for selected columns
        st.write("Summary Statistics for Selected Variables:")
        st.write(df[selected_columns].describe())

        # Check skewness for selected columns
        st.write("The skewness values for selected variables are:")
        st.write(df[selected_columns].skew())

        # Check kurtosis for selected columns
        st.write("The kurtosis values for selected variables are:")
        st.write(df[selected_columns].kurt())

        # Line chart for the selected columns
        for column in selected_columns:
            st.write(f"The line chart for {column}:")
            st.line_chart(df[column])

        # Bar chart for the selected columns
        for column in selected_columns:
            st.write(f"The bar chart for {column}:")
            st.bar_chart(df[column])

        # Area chart for the selected columns
        for column in selected_columns:
            st.write(f"The area chart for {column}:")
            st.area_chart(df[column])

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
if not st.session_state.clicked_button:
    if st.button("Let's get started", on_click=clicked):
        st.session_state.clicked_button = True

# Check if the button was clicked
if st.session_state.clicked_button:
    df = st.file_uploader('Upload your CSV file here', type="csv")
    if df is not None:
        df = pd.read_csv(df)
        analyze_data(df)
