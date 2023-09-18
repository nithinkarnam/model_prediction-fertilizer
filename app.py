import pickle
import streamlit as st

# Load the pickled model
pickled_model = pickle.load(open('model.pkl', 'rb'))

# Background Image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.ugaoo.com/cdn/shop/articles/shutterstock_301313486.jpg?v=1661870861");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dark Theme
st.markdown(
    """
    <style>
    .stSidebar {
        background-color: #121212;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Fertilizer Recommendation App")
st.subheader("Predict the Recommended Fertilizer for Your Crops")

# Create sidebar options
st.sidebar.header('Parameters')
st.sidebar.write('Adjust the sliders and select options to predict the recommended fertilizer for your crops.')

temperature = st.sidebar.slider("Temperature (°C)", -30, 50, 25)
humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
moisture = st.sidebar.slider("Moisture Level", 0, 100, 50)
soil_type = st.sidebar.selectbox("Select Soil Type", ['Loamy', 'Sandy', 'Clayey', 'Black', 'Red'])
crop_type = st.sidebar.selectbox("Select Crop Type", ['Sugarcane', 'Cotton', 'Millets', 'Paddy', 'Pulses', 'Wheat', 'Tobacco', 'Barley', 'Oil seeds', 'Ground Nuts', 'Maize'])
nitrogen = st.sidebar.slider("Nitrogen Content (ppm)", 0, 200, 100, step=5)
potassium = st.sidebar.slider("Potassium Content (ppm)", 0, 200, 100, step=5)
phosphorous = st.sidebar.slider("Phosphorous Content (ppm)", 0, 200, 100, step=5)

# Map user inputs to model features
soil_mapping = {'Loamy': 0, 'Sandy': 1, 'Clayey': 2, 'Black': 3, 'Red': 4}
crop_mapping = {'Sugarcane': 0, 'Cotton': 1, 'Millets': 2, 'Paddy': 3, 'Pulses': 4, 'Wheat': 5, 'Tobacco': 6, 'Barley': 7, 'Oil seeds': 8, 'Ground Nuts': 9, 'Maize': 10}

user_input = {
    'Moisture': moisture,
    'Soil Type': soil_mapping[soil_type],
    'Crop Type': crop_mapping[crop_type],
    'Nitrogen': nitrogen,
    'Potassium': potassium,
    'Phosphorous': phosphorous
}

user_df = pd.DataFrame([user_input])

# Predict Fertilizer
if st.sidebar.button("Predict"):
    prediction = pickled_model.predict(user_df)

    # Map the predicted value to a fertilizer type
    fertilizer_types = {
        0: 'Urea',
        5: 'GROMOR 17-17-17',
        4: 'GROMOR 20-20',
        1: 'DAP',
        2: 'GROMOR 28-28',
        3: 'GROMOR 14-35-14',
        6: 'GROMOR 10-26-26'
    }

    recommended_fertilizer = fertilizer_types[prediction[0]]
    st.success(f"The recommended fertilizer for your crops is: {recommended_fertilizer}")
