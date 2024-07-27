import streamlit as st
import pickle

def run():
    st.header("Make Energy Prediction")
    
    # Input for temperature in Celsius
    temperature = st.slider("Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
    
    # Input for humidity in percentage
    humidity = st.slider("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    
    # Input for load in MW
    load = st.number_input("Load (MW)", min_value=0.0)
    
    time_period = st.slider("Time Period (Months)", min_value=1, max_value=12, step=3)

    
    if st.button("View Graph"):
        # Load the model
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Make prediction
        features = [[temperature, humidity, load, time_period]]
        prediction = model.predict(features)
        
        # Display prediction result
        st.write(f"Predicted energy usage for the next {time_period} months:")
        st.write(prediction)
        # Add code to display the prediction graph if necessary

if __name__ == "__main__":
    run()
