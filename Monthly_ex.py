import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.title("Monthly Expenses")


if "my_df" not in st.session_state:
    st.session_state["my_df"] = pd.DataFrame(columns=["Things", "Cost"])


uploaded_file = st.file_uploader("upload your expenses.csv file", type=["csv"])


if uploaded_file is not None and st.session_state["my_df"].empty:
    st.session_state["my_df"] = pd.read_csv(uploaded_file)
    st.rerun() 


df = st.session_state["my_df"]

st.header("Add Expenses")
things = st.text_input("enter the thing")
cost = st.number_input("Enter the cost", min_value=0.0, step=1.0)

if st.button("Save Expenses"):
    if things:
        cost = float(cost)
        
        # Check if item exists and add to it, or append a new row
        if things in df["Things"].values:
            df.loc[df["Things"] == things, "Cost"] += cost
        else:
            new_row = pd.DataFrame({"Things": [things], "Cost": [cost]})
            df = pd.concat([df, new_row], ignore_index=True)
            
        
        st.session_state["my_df"] = df
        st.success("Data saved successfully")
        st.rerun()
    else:
        st.error("First enter the things")


if not df.empty:          
    if st.button("Show chart"):
        fig = px.bar(df, x="Things", y="Cost", title="My Monthly Expenses")
        st.plotly_chart(fig)
        
    if st.button("Pie chart"):
        fig1 = px.pie(df, names="Things", values="Cost", title="Expenses Distribution")
        st.plotly_chart(fig1)
        
st.markdown("_")
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Updated CSV",
    data=csv_data,
    file_name="expenses.csv",
    mime="text/csv"
)