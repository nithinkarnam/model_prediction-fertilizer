import pickle
import streamlit as st

# Load the pickled model
pickled_model = pickle.load(open('ferti.pkl', 'rb'))

# Define soil and crop options
soil_options = {
    'Loamy': 2,
    'Sandy': 4,
    'Clayey': 1,
    'Black': 0,
    'Red': 3
}

crop_options = {
    'Sugarcane': 8,
    'Cotton': 1,
    'Millets': 4,
    'Paddy': 6,
    'Pulses': 7,
    'Wheat': 10,
    'Tobacco': 9,
    'Barley': 0,
    'Oil seeds': 5,
    'Ground Nuts': 2,
    'Other': 3
}


def main():
    st.set_page_config(page_title="Fertilizer Forecast App", page_icon=":farm:", layout="wide")
    st.title("Fertilizer Prediction")

    # Create sidebar options
    st.sidebar.header('Parameters')
    st.sidebar.write('Adjust the sliders and select options to predict the recommended fertilizer for your crops.')

    # Increase the size of the parameter inputs
    temp = st.sidebar.slider("Temperature (in Celsius)", -30, 50, 25, key="temp")
    hum = st.sidebar.slider("Humidity", 0, 100, 50, key="hum")
    nitrogen = st.sidebar.slider("Nitrogen Content in Soil", 0, 200, 100, step=5, key="nitrogen")
    potassium = st.sidebar.slider("Potassium Content in Soil", 0, 200, 100, step=5, key="potassium")
    phosphorous = st.sidebar.slider("Phosphorous Content in Soil", 0, 200, 100, step=5, key="phosphorous")

    soil_type = st.sidebar.selectbox(
        "Select Soil Type",
        list(soil_options.keys()),
        key="soil_type"
    )

    crop_type = st.sidebar.selectbox(
        "Select Crop Type",
        list(crop_options.keys()),
        key="crop_type"
    )

    # Get the soil and crop parameters
    soil_param = soil_options[soil_type]
    crop_param = crop_options[crop_type]

    inputs = [[temp, hum, soil_param, crop_param, nitrogen, potassium, phosphorous]]

    if st.sidebar.button("Predict"):
        prediction = pickled_model.predict(inputs)

        # Map the predicted value to a fertilizer type
        fertilizer_types = {
            0: "UREA",
            1: "DAP",
            2: "GROMOR 28-28",
            3: "GROMOR 14-35-14",
            4: "GROMOR 20-20",
            5: "GROMOR 17-17-17",
            6: "GROMOR 10-26-26",
        }

        result = fertilizer_types[prediction[0]]

        # Display the output
        st.header('Output')
        st.success(f"The recommended fertilizer for your crops is: {result}")

    
    st.image("https://st.adda247.com/https://wpassets.adda247.com/wp-content/uploads/multisite/sites/5/2022/05/26151136/Fertilizers.png", use_column_width=True)
    st.write("Harvesting Success: Accurate Fertilizer Predictions for Sustainable Agriculture")
    
    st.image("https://www.ugaoo.com/cdn/shop/articles/shutterstock_301313486.jpg?v=1661870861", use_column_width=True)
    st.write("FARMING NEVER HARMS")

if __name__ == '__main__':
    main()
