import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

    # Center the input parameters
    input_col, output_col = st.beta_columns([2, 1])

    # Create sidebar options
    with input_col:
        st.header('Parameters')
        st.write('Adjust the sliders and select options to predict the recommended fertilizer for your crops.')
        temp = st.slider("Temperature (in Celsius)", -30, 50, 25)
        hum = st.slider("Humidity", 0, 100, 50)
        nitrogen = st.slider("Nitrogen Content in Soil", 0, 200, 100, step=5)
        potassium = st.slider("Potassium Content in Soil", 0, 200, 100, step=5)
        phosphorous = st.slider("Phosphorous Content in Soil", 0, 200, 100, step=5)

        soil_type = st.selectbox(
            "Select Soil Type",
            list(soil_options.keys())
        )

        crop_type = st.selectbox(
            "Select Crop Type",
            list(crop_options.keys())
        )

        # Get the soil and crop parameters
        soil_param = soil_options[soil_type]
        crop_param = crop_options[crop_type]

        inputs = [[temp, hum, soil_param, crop_param, nitrogen, potassium, phosphorous]]

        if st.button("Predict"):
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

    # Display the output as a pie chart
    with output_col:
        st.header('Output')
        st.write(f"The recommended fertilizer for your crops is: {result}")

        # Create a pie chart
        labels = list(fertilizer_types.values())
        sizes = np.ones(len(labels))
        sizes[prediction[0]] = 1.2  # Highlight the recommended fertilizer
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)

if __name__ == '__main__':
    main()
