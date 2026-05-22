ECHO is on.
import streamlit as st
import pandas as pd
import numpy as np

# page configuration
st.set_page_config(
    page_title="dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Student Performance Dashboard")
st.write("This is the sample Dashboard")

data = {
    "T1": [66, 89, 78, 92],
    "T2": [91, 68, 68, 82],
    "T3": [76, 99, 68, 82],
}

df = pd.DataFrame(data, index=["s1", "s2", "s3", "s4"])

st.subheader("Marks Card")
st.dataframe(df)

st.subheader("Performance Chart")
st.line_chart(df.T)
