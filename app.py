import streamlit as st

def main():
    st.title("Energy and Sales Forecasting")

    # Main page layout
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Select Section", ["Energy", "Sales"])
    action = st.sidebar.radio("Select Action", ["Analyze Previous Data", "Make Prediction"])

    if section == "Energy":
        if action == "Analyze Previous Data":
            import pages.energy_analyze as energy_analyze
            energy_analyze.run()
        else:
            import pages.energy_predict as energy_predict
            energy_predict.run()
    else:
        if action == "Analyze Previous Data":
            import pages.sales_analyze as sales_analyze
            sales_analyze.run()
        else:
            import pages.sales_predict as sales_predict
            sales_predict.run()

if __name__ == "__main__":
    main()
    
# streamlit run C:\Users\5EIN\OneDrive\Desktop\woodpecker\woodpecker-hackathon\app.py