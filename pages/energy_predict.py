import streamlit as st
import pickle

def run():
    st.header("Make Energy Prediction")
    
    # Checkbox to include temperature
    include_temperature = st.checkbox("Include Temperature")
    if include_temperature:
        temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0, step=0.1)
    else:
        temperature = None
    
    # Checkbox to include humidity
    include_humidity = st.checkbox("Include Humidity")
    if include_humidity:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
    else:
        humidity = None

    # Checkbox to include load
    include_load = st.checkbox("Include Load")
    if include_load:
        load = st.number_input("Load (MW)", min_value=0.0)
    else:
        load = None
    
    # Input for time period in months
    time_period = st.slider("Time Period (Months)", min_value=1, max_value=12, step=3)
    
    if st.button("View Graph"):
        # Load the model
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        
        # Prepare features for prediction
        features = [time_period]
        if include_load:
            features.insert(0, load)
        if include_humidity:
            features.insert(0 if not include_load else 1, humidity)
        if include_temperature:
            features.insert(0 if not include_load and not include_humidity else (1 if include_load else 1), temperature)
        
        # Reshape features to fit model's expected input
        features = [features]
        
        # Make prediction
        prediction = model.predict(features)
        
        # Display prediction result
        st.write(f"Predicted energy usage for the next {time_period} months:")
        st.write(prediction)
        # Add code to display the prediction graph if necessary

if __name__ == "__main__":
    run()
