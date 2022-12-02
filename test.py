import streamlit as st
import pandas as pd

def Customer():

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
                df.to_csv('customers.csv', mode='a', index=False, header=False)

        with col2:

            st.subheader("Customer dataset")
            st.text("Table containing customer information: ")

            customer_data = get_Data('customers.csv')
            st.write(customer_data)


def Product():

    header = st.container()
    inputs = st.container()

    def get_Data(filename):
        data = pd.read_csv(filename)
        return data

    with header:
        st.title("Product Information")
        st.text("In this page you are able to input and access product information.")

    with inputs:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Data input")

            Name = st.text_input("Enter product name: ")
            Stock = st.slider("Enter product stock: ")
            Price = st.number_input("Enter product price: ", step=100)

            new_data = [[Name, Stock, Price]]

            df = pd.DataFrame(new_data)
            if(st.button("Submit")):
                df.to_csv('products.csv', mode='a', index=False, header=False)

        with col2:

            st.subheader("Product dataset")
            st.text("Table containing product information: ")

            product_data = get_Data('products.csv')
            st.write(product_data)

def Purchase():
    st.title("Purchase Information")
    
all_Pages = {
    "Customer": Customer,
    "Product": Product,
    "Purchase": Purchase
}

st.sidebar.title("Python Website")
st.sidebar.header("Databse structure")

selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
all_Pages[selected_page]()





