import streamlit as st
import pandas as pd

header = st.container()
inputs = st.container()

def get_Data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.title("Customer Information")
    st.text("In this page you are able to input and access customer information.")

with inputs:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Data input")

        Name = st.text_input("Enter customer name: ")
        Address = st.text_input("Enter customer address: ")
        Phone_Number = st.text_input("Enter customer phone number: ")

        new_data = [[Name, Address, Phone_Number]]

        df = pd.DataFrame(new_data)
        if(st.button("Submit")):
            df.to_csv('dataset.csv', mode='a', index=False, header=False)

    with col2:

        st.subheader("My dataset")
        st.text("On this dataset I am going to show customer, products and purchase information")

        customer_data = get_Data('dataset.csv')
        st.write(customer_data)
