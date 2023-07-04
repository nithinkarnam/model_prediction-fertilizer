import pickle
import streamlit as st 

# load the pickled model
pickled_model = pickle.load(open('ferti.pkl', 'rb'))

# define soil and crop options
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

    # create sidebar options
    st.sidebar.header('Parameters')
    temp = st.sidebar.slider("Temperature (in Celsius)", -30, 50, 25)
    hum = st.sidebar.slider("Humidity", 0, 100, 50)
    nitrogen = st.sidebar.slider("Nitrogen Content in Soil", 0, 200, 100, step=5)
    potassium = st.sidebar.slider("Potassium Content in Soil", 0, 200, 100, step=5)
    phosphorous = st.sidebar.slider("Phosphorous Content in Soil", 0, 200, 100, step=5)

    soil_type = st.sidebar.selectbox(
        "Select Soil Type",
        list(soil_options.keys())
    )

    crop_type = st.sidebar.selectbox(
        "Select Crop Type",
        list(crop_options.keys())
    )

    # get the soil and crop parameters
    soil_param = soil_options[soil_type]
    crop_param = crop_options[crop_type]

    inputs = [[temp, hum, soil_param, crop_param, nitrogen, potassium, phosphorous]]

    if st.sidebar.button("Predict"):
        prediction = pickled_model.predict(inputs)

        # map the predicted value to fertilizer type
        fertilizer_types = {
            0: "10-26-26",
            1: "14-35-14",
            2: "17-17-17",
            3: "20-20",
            4: "28-28",
            5: "DAP",
            6: "Urea"
        }

        result = fertilizer_types[prediction[0]]
        st.success(f"Fertilizer recommended: {result}")

if __name__ == '__main__':
    main()
