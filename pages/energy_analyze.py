import streamlit as st
from PIL import Image

def run():
    st.header("Analyze Previous Energy Data")
    # Load images
    correlation_heatmap_image = Image.open(r"C:\Users\5EIN\OneDrive\Desktop\woodpecker\woodpecker-hackathon\pages\images\correlation_heatmap.jpg")
    temperature_over_time_image = Image.open(r"C:\Users\5EIN\OneDrive\Desktop\woodpecker\woodpecker-hackathon\pages\images\energy_over_time.jpg")
    energy_over_time_image = Image.open(r"C:\Users\5EIN\OneDrive\Desktop\woodpecker\woodpecker-hackathon\pages\images\humidity_over_time.jpg")
    humidity_over_time_image = Image.open(r"C:\Users\5EIN\OneDrive\Desktop\woodpecker\woodpecker-hackathon\pages\images\temperature_over_time.jpg")
    
    # Display buttons and corresponding images
    if st.button("Correlation Heatmap"):
        st.image(correlation_heatmap_image, caption='Correlation Heatmap')
    
    if st.button("Max Temperature and Min Temperature Over Time"):
        st.image(temperature_over_time_image, caption='Max and Min Temperature Over Time')
    
    if st.button("SEWA Energy/hr Over Time"):
        st.image(energy_over_time_image, caption='SEWA Energy/hr Over Time')
    
    if st.button("Max Humidity and Min Humidity Over Time"):
        st.image(humidity_over_time_image, caption='Max and Min Humidity Over Time')

if __name__ == "__main__":
    run()
    
    

