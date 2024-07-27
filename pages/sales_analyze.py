import streamlit as st

def run():
    st.header("Analyze Previous Sales Data")
    time_period = st.selectbox("Select Time Period", ["Last Week", "Last Month", "Last Year"])
    if st.button("View Graph"):
        st.write(f"Displaying sales data for {time_period}.")
        # Add code to display the graph
