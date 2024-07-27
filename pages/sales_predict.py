import streamlit as st
import pickle

def run():
    st.header("Make Sales Prediction")
    
    # Input for store number (integer)
    store_no = st.number_input("Store No.", min_value=1, step=1)
    
    # Input for item number (integer)
    item_no = st.number_input("Item No.", min_value=1, step=1)
    
    # Input for time period in months
    time_period = st.slider("Time Period (Months)", min_value=1, max_value=12, step=3)
    
    if st.button("View Graph"):
        # Load the model
        with open('sales_model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Make prediction
        features = [[store_no, item_no, time_period]]
        prediction = model.predict(features)
        
        # Display prediction result
        st.write(f"Predicted sales for store {store_no}, item {item_no} for the next {time_period} months:")
        st.write(prediction)
        # Add code to display the prediction graph if necessary

if __name__ == "__main__":
    run()
