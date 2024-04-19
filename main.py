import streamlit as st
import pandas as pd

# Initialize session state
if 'clicked_button' not in st.session_state:
    st.session_state.clicked_button = False

# Function to update session state
def clicked():
    st.session_state.clicked_button = True

# title 
st.title("AI Assistant for Data Science 🤖")

# welcoming message 
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
    
    # divider to create a line between the two sections
    st.divider()
    
    # caption to add text in the center
    st.caption("<p style='text-align:center'>Designed and Developed by 🫱🏻‍🫲🏼: Japanjot Singh</p>", unsafe_allow_html=True)

# Button to initiate the process
if not st.session_state.clicked_button:
    if st.button("Let's get started", on_click=clicked):
        st.session_state.clicked_button = True

# Check if the button was clicked
if st.session_state.clicked_button:
    df = st.file_uploader('Upload your CSV file here', type="csv")
    if df is not None:
        df.seek(0)
        df = pd.read_csv(df, low_memory=False)

        # Main Function
        def main(): 
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

            # Check the unique values in the dataset
            st.write("The unique values in your dataset are:")
            st.write(df.nunique())  

            # Check the duplicate values in the dataset
            st.write("The duplicate values in your dataset are:")
            st.write(df.duplicated().sum()) 

            # Check the statistical values in the dataset
            st.write("The statistical values in your dataset are:")
            st.write(df.describe())  

            # Check the correlation values in the dataset
            st.write("**Correlation Analysis**")
            st.write("Select variables to calculate correlation:")
            columns = df.columns
            selected_columns = st.multiselect("Select variables", columns)
            if len(selected_columns) > 0:
                numeric_columns = df.select_dtypes(include=['number']).columns
                selected_numeric_columns = [col for col in selected_columns if col in numeric_columns]
                if selected_numeric_columns:
                    correlation = df[selected_numeric_columns].corr()
                    st.write(correlation)
                else:
                    st.write("Please select numeric variables for correlation calculation.")

            # Check the skewness values in the dataset
            st.write("The skewness values in your dataset are:")
            st.write(df.skew()) 

            # Check the kurtosis values in the dataset
            st.write("The kurtosis values in your dataset are:")
            st.write(df.kurt())

            # Line chart for the data 
            st.write("The line chart for your dataset is:")
            user_column = st.selectbox("Select the column for line chart", df.columns)
            st.line_chart(df, y=[user_column]) 

            # Bar chart for the data
            st.write("The bar chart for your dataset is:")
            user_column = st.selectbox("Select the column for bar chart", df.columns)
            st.bar_chart(df, y=[user_column])

            # Area chart for the data
            st.write("The area chart for your dataset is:")
            user_column = st.selectbox("Select the column for area chart", df.columns)
            st.area_chart(df, y=[user_column])

            # How to display special data in streamlit
            st.write("The Special description for your dataset is given below in the information section:")

        main()
