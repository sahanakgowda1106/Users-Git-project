import streamlit as st
import pandas as pd

st.title("🔐 User Login")

file = "users.csv"

# Load users dataset
try:
    df = pd.read_csv(file)
except:
    st.error("users.csv file not found")
    st.stop()

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    user = df[(df["Username"] == username) & (df["Password"] == password)]

    if not user.empty:
        st.success("✅ Login Successful!")
        st.write("Welcome,", username)

        # show user details
        st.subheader("Your Details")
        st.dataframe(user)

    else:
        st.error("❌ Invalid Username or Password")