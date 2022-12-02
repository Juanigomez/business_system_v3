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

            Name = str(st.text_input("Enter customer name: "))
            Address = st.text_input("Enter customer address: ")
            Phone_Number = st.text_input("Enter customer phone number: ")

            customer_input_btn = st.button("Submit")
            if customer_input_btn:

                dataset = pd.read_csv('customers.csv')
                all_Customers = list(dataset.iloc[:,0])
                index = 0
                count = int(len(all_Customers) - 1)
                
                if Name != all_Customers[index]:
                    for clients in all_Customers:
                        while Name != all_Customers[index]:
                            if index == count:
                                break
                            else:
                                index += 1

                if Name == all_Customers[index]:
                    global current_Customer
                    current_Customer = Name
                    st.info(f"Known customer {Name}")

                else:
                    new_data = [[Name, Address, Phone_Number]]
                    df = pd.DataFrame(new_data)
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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Customer Info.")
        st.text_input("Enter customer name: ")

    with col2:
        st.subheader("Product Info.")
        product = st.text_input("Enter product name: ")
        amount = st.slider("Amount", 1, 50)

    with col3:
        st.subheader("Payment Info.")
        method = st.selectbox("Select payment method", ['cash', 'debit', 'credit'])
        cuotas = st.slider("Cuotas", 1, 12)
        discount = st.selectbox("Select discount", ['None', 'Itau(25%)'])

all_Pages = {
    "Customer": Customer,
    "Product": Product,
    "Purchase": Purchase
}

st.sidebar.title("Python Website")
st.sidebar.header("Databse structure")

selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
all_Pages[selected_page]()



