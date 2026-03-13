import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="User Dashboard", layout="wide")

st.title("👥 User Registration Dashboard")

# Load dataset
df = pd.read_csv("users.csv")

# Show dataset
st.subheader("📊 Users Dataset")
st.dataframe(df)

# Metrics
st.subheader("📈 Dashboard Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Users", len(df))
col2.metric("Total Countries", df["Country"].nunique())
col3.metric("Latest User ID", df["User_ID"].max())

# Sidebar filters
st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + list(df["Country"].unique())
)

# Apply filter
if country != "All":
    filtered_df = df[df["Country"] == country]
else:
    filtered_df = df

st.subheader("Filtered Users")
st.dataframe(filtered_df)

# Search user
st.subheader("🔍 Search User")

search = st.text_input("Enter Username")

if search:
    result = df[df["Username"].str.contains(search, case=False)]
    st.dataframe(result)

# Registration chart
st.subheader("📅 Registrations Over Time")

df["Registration_Date"] = pd.to_datetime(df["Registration_Date"])

chart_data = df.groupby("Registration_Date").size()

st.line_chart(chart_data)