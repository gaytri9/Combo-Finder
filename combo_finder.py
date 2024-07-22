iimport random as r
import streamlit as st
import pandas as pd

# Title
st.title('Product Combination Finder')

# File upload
file = st.file_uploader("Upload a CSV file with Product and Price columns")

# Input fields for lower and upper limits
lower_limit = st.number_input("Lower Limit", min_value=0, value=290)
upper_limit = st.number_input("Upper Limit", min_value=lower_limit, value=310)

# Email input
email = st.text_input("Email Id")

# Submit button
if st.button("Submit"):
    if file is not None and email:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Convert the dataframe to a dictionary
        ProductList = pd.Series(df.Price.values, index=df.Product).to_dict()
        
        # Initialize variables
        ResultList = set()
        iterations = 1000
        

        
        # Loop till number of iterations
        for _ in range(iterations):

            # Select combo size (i.e. number of products in a combo)
            SetSize = r.randint(2, len(ProductList)-1)
            # Select a random combination of products
            ComboList = r.sample(list(ProductList.keys()), set_size)
            ComboList.sort()
            
            # Calculate sum of products in a combo
            ComboSum = sum([ProductList[i] for i in ComboList])
            
            # Check the sum between lower and upper bounds
            if lower_limit <= ComboSum <= upper_limit:
                # Add to result list as a frozenset (immutable and hashable)
                ResultList.add(frozenset(ComboList))
        
        # Print the result list
        st.write("Combinations found:")
        for combo in ResultList:
            st.write(combo)
        
        # Print the length of the result list
        st.write("Number of unique combinations that sum between the limits:", len(ResultList))
    else:
        st.error("Please upload a file and enter a valid email address.")
