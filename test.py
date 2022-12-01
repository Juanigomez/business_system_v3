import streamlit as st
import pandas as pd

header = st.container()
inputs = st.container()
dataset = st.container()

def get_Data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.title("Welcome to my test app")
    st.text("In this project I am going to sketch the v2.2 of nmy business system")

with inputs:
    st.header("Data input")

    Name = st.text_input("Enter customer name: ")
    Address = st.text_input("Enter customer address: ")
    Phone_Number = st.text_input("Enter customer phone number: ")

    new_data = [[Name, Address, Phone_Number]]

    df = pd.DataFrame(new_data)
    if(st.button("Submit")):
        df.to_csv('data/dataset.csv', mode='a', index=False, header=False)

with dataset:
    st.header("My datset")
    st.text("On this dataset I am going to show customer, products and purchase information")

    customer_data = get_Data('dataset.csv')
    st.write(customer_data)
