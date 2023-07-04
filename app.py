import streamlit as st

def main():
    # Add CSS for the background and tree animations
    st.markdown(
        """
        <style>
        body {
            background-image: url('tree_background.gif');
            background-repeat: repeat-y;
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the width for the sidebar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width: 300px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.set_page_config(
        page_title="Fertilizer Forecast App",
        page_icon=":farm:",
        layout="wide"
    )
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
            0: "Muriate of Potash",
            1: "Sodium Nitrate",
            2: "Zn-EDTA",
            3: "CALCIUM AMMONIUM NITRATE",
            4: "AMMONIA SULPHATE",
            5: "DAP",
            6: "Urea"
        }

        result = fertilizer_types[prediction[0]]
        st.success(f"Fertilizer recommended: {result}")

if __name__ == '__main__':
    main()

